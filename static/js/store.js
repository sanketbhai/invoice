    
$(document).ready(function(){
    
       $('#store').click(function(){
                  alert("insidestore"); //sent
      
if($("#date").val()!==NaN && $("#date").val()!=="" && $("#provider").val()!==NaN && $("#provider").val()!=="" && $("#provider_rep").val()!==NaN && $("#provider_rep").val()!=="" && $("#provider_info").val()!==NaN && $("#provider_info").val()!=="" && $("#Customer_name").val()!==NaN && $("#Customer_name").val()!==""&& $("#Customer_address").val()!==NaN && $("#Customer_address").val()!=="" && $("#user").val()!==NaN && $("#user").val()!=="" && $("#invoice_no").text()!==NaN && $("#invoice_no").text()!==""){
                 var prolist=[];
                var prilist=[];
                var qtylist=[];
                var totlist=[];
            alert("insidestore on click lodt crated");
            $('tbody').children().each(function(){ 
                alert("inside tbody");
                
                var r=$(this);
                
        
                var total=r.find('.total').text();
                var product=r.find('.product').val();
                var price=r.find('.price').val();
                var qty=r.find('.qty').val();
                alert("below values assi");
                
            if (product!==NaN && product!==""){
                
                if (total!==NaN && total!==""){
                    alert("inside both if");
                    
                    
                    
                    //this if statment is going to send values using json
                    prolist.push(product);
                    prilist.push(price);
                    qtylist.push(qty);
                    totlist.push(total);
                    
                    
                }//end if
            }//end of product vala if
            });
            alert("autside loop");
            //sending lists to route
            var dic={ 
                        pro:prolist,
                        pri:prilist,
                        qt:qtylist,
                        tot:totlist,
                        date:$("#date").val(),
                        provider:$("#provider").val(),
    
                        provider_rep:$("#provider_rep").val(),
                        provider_info:$("#provider_info").val(),       
                        customer_name:$("#Customer_name").val(),
                        customer_address:$("#Customer_address").val(),
                        user:$("#user").val(),
                        invoice_no:$("#invoice_no").text()
     
                    };
                    alert(dic);
                    new_dict = JSON.stringify(dic);
                    alert("sring is created");
                    $.getJSON('/store',{dic:new_dict,});
                    alert("below json");
            }//big if
            else{
                alert("some fields are empty")
            }
      
       });
        
})