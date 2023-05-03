//get the value selected from Dropdownlist
function getValueSelected(element)
{
  var e = document.getElementById(element);
  var value = e.value;
  var text = e.options[e.selectedIndex].text;

  return value;
}

//get Exchange
function getExchange(){

  var selFrom = getValueSelected("selFrom");
  var selTo = getValueSelected("selTo");
  var amount = document.getElementById("inpAmount");

  $.ajax({
    url: 'http://localhost:5000/getExchange',
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify({
      amount:amount.value,
      from:selFrom,
      to:selTo
    }),
    dataType: "json",

    success: function (response) {
     
      jsonObj = JSON.stringify(response);
      var json = JSON.parse(jsonObj);

      var lfrom =document.getElementById("lfrom");
      lfrom.innerHTML = json.rateFrom

      var lto =document.getElementById("lto");
      lto.innerHTML = json.rateTo

      var lresult =document.getElementById("lresult");
      lresult.innerHTML = json.result

    },
    failure: function (response) {
      alert("Failure getting the exchange: "+response);

    },
    error: function (response) {
      console.log("Error getting the exchange: "+response);

    }
    
  });


}

//populate the Dropdownlist
function dynamicDropdownList(codes){
 
  var selFromList = document.getElementById("selFrom");
  var selToList = document.getElementById("selTo");
 
  var json = JSON.parse(codes);
 
  for(var i=0;i<json.supported_codes.length;i++)
  {     
      var optFrom = document.createElement("option"); 
      optFrom.text = json.supported_codes[i][0] +" - " + json.supported_codes[i][1];
      optFrom.value = json.supported_codes[i][0];
      selFromList.options.add(optFrom); 

      var optTo = document.createElement("option"); 
      optTo.text = json.supported_codes[i][0] +" - " + json.supported_codes[i][1];
      optTo.value = json.supported_codes[i][0];
      selToList.options.add(optTo);
  } 
    
}     

(function() {
   
        var jsonObj;
        var data;
        var stringify, obj;
    
        $.ajax({
            url: 'http://localhost:5000/getCodes',
            type: 'GET',
            dataType: "json",
            data: {
              data: data
            },
            async:true,
            crossDomain:true,
            success: function(response, status, xhr) {

              jsonObj = JSON.stringify(response);
              dynamicDropdownList(jsonObj);
            },
            failure: function (response) {
              alert("Failure getting the Codes: ");
        
            },
            error: function (response) {
              alert("Error getting the Codes: ");
        
            }

          });
 })();

 
 



