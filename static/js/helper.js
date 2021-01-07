let eventHandler = {
    enableSubmitButtion: function() {
        $('input#submit-button').prop('disabled', false);
    },

    showSection: function(section_id) {
        $('section#' + section_id).fadeIn();
        $("html,body").animate({scrollTop:$('section#' + section_id).offset().top});
    }
}

$(function(){
    $('a#search-button').click(function() {
        eventHandler.enableSubmitButtion();
    });

    $('a#downloader').click(function() {
        $('a#next').removeClass('disabled-link');
    });

    if(document.location.href.endsWith('/practice')) {
        $('input[name=reason]').val('本番タスクではここに根拠を入力してください');
        $('input[name=reason]').prop('readonly', true);
    }
});

var Helper = Helper || {};

Helper.getRandomString = function() {
    let chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_0123456789';
    let length = 35;
    var text = '';
    for(var i = 0; i < length; i++){
        text += chars[Math.floor(Math.random() * chars.length)];
    }
    return text + Date.now();
}
