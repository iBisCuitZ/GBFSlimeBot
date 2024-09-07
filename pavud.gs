function myBrunS() {
    if (!prevlogin){
        SpreadsheetApp.getActiveSpreadsheet().getSheetByName("AngBao").getRange('j3').setValue('=RANDBETWEEN(1,6)');
    }
    else {
        ui.alert("already play")
    }
}

function prevlogin() {
  const ps=PropertiesService.getUserProperties();
  const userEmail=e.user.getEmail();
  let lastlogin=ps.getProperty(userEmail);
  if(!lastlogin) {
    ps.setProperty(userEmail,date)
    return false;
  }else {
    return true;
  }
}
