$(document).ready(function(){
    
    rnum=0
    
    $('#addRow').click(function(){
        $('tbody').append('<tr id="R${++rnum}"><td> <p> no${rnum}</p></td><td><input type="text/submit/hidden/button/image" name="product" id="product" value="" /></td> <td><input type="text/submit/hidden/button/image" name="p/item"id="p/item" value="" /></td> <td><input type="text/submit/hidden/button/image" name="qnt" id="qnt" value="" /></td><td><input type="text/submit/hidden/button/image" name="prise" id="prise" value="" /></td></tr>');
        
        });
    $('#removeRow').click(function(){
        $('tbody tr:last').remove();
    })
})