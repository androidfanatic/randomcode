// ==UserScript==
// @name         Delete comments
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Delete comments
// @author       X
// @match        https://www.reddit.com/user/<reddit-username>/
// @grant        none
// ==/UserScript==
/* jshint -W097 */
'use strict';

var delay_ms = 500

window.onload = function(){    
    var i = 0; 
    $('.del-button .yes').each(function(){ 
        var button = $(this); 
        setTimeout( function(){ 
            button.click()
        }, ++i * delay_ms) 
    })
    setTimeout(function(){
        document.location.reload()
    }, i * delay_ms)
}
