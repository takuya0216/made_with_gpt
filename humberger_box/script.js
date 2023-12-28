var open = false;

function Drop(n) {
  var i;
  if (open == false) {
    for (i = n; i < 5; i++) {
      Drp(i);
    }
    open = true;
  } else if (open == true) {
    for (i = n; i < 5; i++) {
      Cls(i);
    }
    open = false;
  }
}

function Drp(n) {
  var elem = document.getElementsByClassName("menu-con")[n];
  var pos = -1 * window.innerWidth - n * 100; // window.innerWidth を使用して幅方向に変更
  var id = setInterval(frame, 5);

  function frame() {
    if (pos >= -10) { // 0 に変更
      clearInterval(id);
      elem.style.left = 0 + 'px';
    } else {
      pos += 10;
      elem.style.left = pos + 'px';
    }
  }
}

function Cls(n) {
  var elems = document.getElementsByClassName("menu-con")[n];
  var poss = 0;
  var ids = setInterval(frames, 5);

  function frames() {
    if (poss <= -1 * window.innerWidth) { // window.innerWidth を使用して幅方向に変更
      clearInterval(ids);
      elems.style.left = -1 * window.innerWidth + 'px';
    } else {
      poss += -7 - n * 2;
      elems.style.left = poss + 'px';
    }
  }
}
