$(document).ready(function(){
    
    var rnum=1;
    
    
    $('#addRow').click(function(){
        (++rnum);
        
        $('tbody').append('<tr><td > <p>'+(rnum)+'</p></td><td><input type="text" name="product" class="databox product" /></td> <td><input type="number" class="databox price"/></td> <td><input type="number"  class="qty" /></td><td class="total"></td></tr>');
        
        
        });
    $('#removeRow').click(function(){

        alert(rnum)
        if (rnum>1) {
            --rnum;
            $('tbody tr:last').remove();
        
    
     var total_amount=0;
        
        
       $('tbody').children().each(function(){ 
                
                    
                var r=$(this);
                
                var t=r.find('.total').text();
                
                if (t!==NaN && t!==""){
                        
                        
                    total_amount+=parseFloat(t);
                        
                    }
                });
                
                $('#total_amount').text(total_amount);  
                    
        }
        
        
    });
    
    
    $('table').on("change","input",function(){ 
        
        var row= $(this).closest('tr');
        var qty=parseFloat(row.find('.qty').val());
        
        var price=parseFloat(row.find('.price').val());
        
        var total=qty*price;
        
        row.find('.total').text(isNaN(total)?"":total);
        
        var total_amount=0;
        
        
        
        $('tbody').children().each(function(){ 
            
            
            var r=$(this);
            
            var t=r.find('.total').text();
            var product=r.find('.product').val();
        if (product!==NaN && product!==""){
            
            if (t!==NaN && t!==""){
                
                
                total_amount+=parseFloat(t);
                
                
                
                
                ;
            }//end if
        }//end of product vala if
        });
        
        $('#total_amount').text(total_amount);
        
    });

    
   
   

    //from here forword writing script for showenvo.html file
    
})

