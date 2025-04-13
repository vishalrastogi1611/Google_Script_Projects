function myFunction() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var LastRow = sheet.getLastRow();
  sheet.getRange("H1").setValue("Profit");

  var SalesRange = sheet.getRange("F2:F"+LastRow);

  var CostRange = sheet.getRange("G2:G"+LastRow);

  var ProfitRange = sheet.getRange("H2:H"+LastRow);

  var SalesValues = SalesRange.getValues();

  var CostValues = CostRange.getValues();

  for(var i=0; i<LastRow; i++){
    ProfitRange.getCell(i+1,1).setValue(SalesValues[i][0]-CostValues[i][0]);

    if(SalesValues[i][0]-CostValues[i][0] < 70){
      var rowtohighlight = i+2;
      sheet.getRange(rowtohighlight,1,1,8).setBackground("#FF0000")
    }
  }

  
}
