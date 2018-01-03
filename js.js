function DropDown() {
	 var x = document.getElementsByClassName("NavContainer");
    
    if (x[0].style.display === "none") {
    	 x[0].style.display = "flex";
    	} else {
    		 x[0].style.display = "none";
    	}
   
}