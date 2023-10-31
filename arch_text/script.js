const textPath = document.getElementById("textPath");
const textCurve = document.querySelector(".text-curve");

textPath.setAttribute("d", "M10 50 Q" + (textCurve.clientWidth / 2) + " -10 " + (textCurve.clientWidth - 10) + " 50");
