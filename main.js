
/* removing this enclosure will allow Dev console invoke and test everything here */
    (function (window) {
    'use strict';

    var FORM_SELECTOR = '[data-coffee-order="form"]';
    var CHECKLIST_SELECTOR = '[data-coffee-order="checklist"]';
    var App = window.App;


  $('#id-select').change(function() {

    console.log("id-select Changed. Value: ", $(this).val(), $('#id-select option:selected').text());
    
   })

   $('#textSelect').click(function() { // When button with #textSelect tag clicked
        console.log("textSelect clicked.");

        // Handles response received from server
        sock.onmessage = function(event) {
            console.log("Server responded DROPDOWN data: " + event.data);

            // parse server response
            var returntext = JSON.parse(event.data);
            console.log("Returned text: ", returntext);

            //
            $('#TestText').text(returntext.TestText);
            $('#TestTitle').text(returntext.Title);

        }

        // Create a JSON object with info and send to server
        var obj = new Object();
        obj.textlength = $('#id-length option:selected').text();
        obj.textgenre = $('#id-genre option:selected').text();

        sock.send(JSON.stringify(obj));
        
    })

   $('#textSubmit').click(function() {

    console.log("textSubmit clicked. Input value: ", $('#textInputBox').val());

    sock.onmessage = function(e) {
        
        console.log("Server responded with: " + e.data);

        // parse the server response
        var response = JSON.parse(e.data);
        //console.log("Speed: ", response.Speed);
        console.log("Time: ", response.Time)

        // Results page update
        
        // Some results fields are filled based on client input (not from server)
        $('#id-type').text($('#id-select option:selected').text());
        var today= new Date().toLocaleString('en-US', { timeZone: 'UTC' });
        $('#id-time').text(today);

        // Some results are from server response
        //$('#id-speed').text(response.Speed);
        //$('#id-error').text(response.Error);

    }
    

    // create a JSON object with info and send to server

    var obj = new Object();
    obj.user_input = $('#textInputBox').val();

    sock.send(JSON.stringify(obj));
    

   })

   var sock = null;
   var wsuri = "ws://127.0.0.1:8081/ws";

   sock = new WebSocket(wsuri);


   window.onload = function() {
    sock = new WebSocket(wsuri);
    console.log("websocket connection with server created");
   }

   sock.onopen = function() {
    console.log("connected to " + wsuri);
    }

    sock.onclose = function(e) {
        console.log("connection closed (" + e.code + ")");
    }


})(window);

