let serverURL = 'https://xxxxxxx';
let logID = Helper.getRandomString();

///////////////////
/*   関数の定義    */
///////////////////
var BrowsingMonitor = BrowsingMonitor || {};

BrowsingMonitor.formatForServer = function(rawData) {
    var finalData = {};
    finalData['id'] = rawData['logID'];
    finalData['project_id'] = rawData['projectID'];
    finalData['user_id'] = rawData['userID'];
    finalData['url'] = rawData['url'];

    if (rawData['referer'] == '')
        finalData['referer'] = 'none';
    else
        finalData['referer'] = rawData['referer'];

    finalData['dwell_time'] = rawData['time']['timeOnPage'];
    finalData['click_count'] = rawData['clicks']['clickCount'];
    finalData['refocus_count'] = 0;
    for (let context of rawData['contextChange']) {
        if (context['type'] == 'visible')
            finalData['refocus_count']++;
    }

    return JSON.stringify(finalData);
}

BrowsingMonitor.sendDataToServer = function(userBehavior) {
    var jsonData = BrowsingMonitor.formatForServer(userBehavior);

    var apiURL = serverURL + 'api/behaviors/';
    var requestType;
    var requestURL;
    if (userBehavior['sendCount'] == 1) {
        requestType = 'POST';
        requestURL = apiURL;
    } else {
        requestType = 'PUT';
        requestURL = apiURL + userBehavior['logID'] + '/';
    }

    // ブラウジング先がログサーバの管理ページでない場合
    if (userBehavior['url'].lastIndexOf(serverURL, 0) < 0) {
        $.ajax({
            url: requestURL,
            type: requestType,
            dataType: 'json',
            contentType: 'application/json',
            data: jsonData,
            timeout: 1000
        }).done(function(data) {; // 通信成功時の処理
        }).fail(function() {
            // 通信失敗時の処理を記述
            console.log('Failed to send a behavior log to a server.');
        });
    }
}


////////////////////////
/*  スクリプトの実行    */
///////////////////////
userLog.init({
    // Available functionality
    clickCount: true,
    clickDetails: false,
    mouseMovement: false,
    context: true,
    keyLogger: false,
    processTime: 3,

    processData: function processData(results) {
        results['projectID'] = projectID;
        results['userID'] = userID;
        results['url'] = location.href;
        results['referer'] = document.referrer;
        results['logID'] = logID;

        if (results['sendCount']) {
            results['sendCount']++;
        } else {
            results['sendCount'] = 1;
        }
        BrowsingMonitor.sendDataToServer(results);
    },

    // Action Item
    actionItem: {
        processOnAction: false,
        selector: '',
        event: ''
    },
});

// タブが閉じられたときにもログデータを出力する
window.addEventListener('beforeunload', function(e) {
    $.when(userLog.processResults()).done(function() {
        return;
    });
}, false);
