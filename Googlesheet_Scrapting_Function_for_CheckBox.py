function onEdit(e) {

  var range = e.range;
  var value = e.value;
  var sheet = range.getSheet();
  var timestamp = new Date();
  var row = range.getRow();
  var col = range.getColumn();
  
  var taskSheet = "Sheet1"; 
  var taskColumn = 2;  
  var taskStatusColumn = 3;          
  var requiredValue = "TRUE";  


  if (sheet.getName() == taskSheet && col == taskColumn) {

    var checkboxRange = sheet.getRange(row,3);
    checkboxRange.insertCheckboxes();
    
  }

  else if (sheet.getName() == taskSheet && col == taskStatusColumn && value == requiredValue) {

    var compltedSheet = e.source.getSheetByName("Sheet2");
    var lr = compltedSheet.getLastRow();
    var targetRange = compltedSheet.getRange(lr+1,1);

    sheet.getRange(row,1,1,3).moveTo(targetRange);
    sheet.deleteRow(row);
    timestamprange = compltedSheet.getRange(lr + 1,4);
    timestamprange.setValue(timestamp);
    
  }

  

}
