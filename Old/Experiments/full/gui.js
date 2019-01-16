/*

TiPod v1.0
Author: graphinghandheld, hymenopus

*/

// Elements

const tiriScript = require("./runTiri")

const stage1 = document.getElementById("stage-1");
const stage1Button = document.getElementById("stage-1-button");

const stage2 = document.getElementById("stage-2");
const networkStatus = document.getElementById("network-status");
const stage2Button = document.getElementById("stage-2-button");

const stage3 = document.getElementById("stage-3");
const stage3Button = document.getElementById("stage-3-button");

const stage4 = document.getElementById("stage-4");
const stage4Button = document.getElementById("stage-4-button");

const stage5 = document.getElementById("stage-5");
const stage5Button = document.getElementById("stage-5-button");

const lockscreen = document.getElementById("lockscreen");
const time = document.getElementById("time");

const home = document.getElementById("home");
const tilesContainer = document.getElementById("tiles-container");

// Variables

var step = 0;

var tiles = [
  {
    title: "Welcome to Tiri Hub",
    text: "Simply say 'hey tiri' or click the microphone icon at the top right corner of the UI and ask Tiri a question!"
  }
];

var homePicture;
var lockPicture;

// Functions

document.getElementById("tiriBtn").onclick = function() {
  tiriScript.startListening();
}

function receiveTiri(whatToReceive) {
  document.getElementById("tiri-container").innerHTML += "<span class='message-return'>" + whatToReceive + "</span>";
}

function saveData() {
  localStorage.lockPicture = lockPicture;
  localStorage.homePicture = homePicture;
}

function loadData() {
  lockPicture = localStorage.lockPicture || "wallpaper.png";
  homePicture = localStorage.homePicture || "wallpaper.png";
  
  updateWallpaper();
}

function updateWallpaper() {
  home.style.backgroundImage = "url(" + homePicture + ")";
  lockscreen.style.backgroundImage = "url(" + lockPicture + ")";
}

function updateTime() {
  var date = new Date();
  
  var hours = date.getHours();
  var minutes = date.getMinutes();
  
  if (hours > 12) {
    hours = hours - 12;
  }
  
  if (minutes < 10) {
    minutes = "0" + minutes;
  }
  
  time.innerText = hours + ":" + minutes;
}

function checkNetwork() {
  if (navigator.onLine == true) {
    networkStatus.innerText = "You're connected, hooray!";
    
    stage2Button.disabled = false;
  } else {
    networkStatus.innerText = "Hmm, it appears you're offline.";
    
    stage2Button.disabled = true;
  }
}

function nextStep() {
  switch (step) {
    case 0:
      stage1.style.display = "none";
      stage2.style.display = "";
      
      checkNetwork();
      
      step = 1;
      
      break;
    case 1:
      stage2.style.display = "none";
      stage3.style.display = "";
      
      step = 2;
      
      break;
    case 2:
      stage3.style.display = "none";
      stage4.style.display = "";
      
      step = 3;
      
      break;
    case 3:
      stage4.style.display = "none";
      stage5.style.display = "";
      
      step = 4;
      
      break;
    case 4:
      loadTiles();
      
      localStorage.setup = true;
      
      stage5.style.display = "none";
      home.style.display = "";
      
      delete step;
      
      break;
  }
}

// Lock Screen Functions

function unlock() {
  loadTiles();
  
  lockscreen.style.display = "none";
  home.style.display = "";
}

// Home Functions

function startTiri() {
  if (document.getElementById("tiles-container").style.display == "block" || document.getElementById("tiles-container").style.display == "") {
    document.getElementById("tiles-container").style.display = "none";
    document.getElementById("tiri").style.display = "block";
    document.getElementById("start-tiri-mic").src = "Close.png"
  } else {
    document.getElementById("tiles-container").style.display = "block";
    document.getElementById("tiri").style.display = "none";
    document.getElementById("start-tiri-mic").src = "TiriMic.png"
  }
}

function loadTiles() {
  document.getElementById("tiles-container").innerHTML = "";
  for (var i = 0; i < tiles.length; i++) {
    let tile = document.createElement("div");
    let tileContent = document.createElement("div");
    let tileTitle = document.createElement("h2");
    let tileText = document.createElement("p");
    
    let backButton = document.createElement("button");
    
    tileTitle.innerText = tiles[i].title;
    tileText.innerText = tiles[i].text;
    
    backButton.innerText = "Back";
    
    tileContent.classList.add("tile");
    backButton.classList.add("tile-back-button");
    
    backButton.style.display = "none";
    
    tileContent.addEventListener("click", function() {
      tileContent.classList.add("clicked");
      
      backButton.style.display = "";
    });
    
    backButton.addEventListener("click", function() {
      backButton.style.display = "none";
      
      tileContent.classList.remove("clicked");
    });
    
    tileContent.appendChild(tileTitle);
    tileContent.appendChild(tileText);
    
    tile.appendChild(tileContent);
    tile.appendChild(backButton);
    
    tilesContainer.prepend(tile);
  }
}

// Event Listeners

stage1Button.addEventListener("click", nextStep);
stage2Button.addEventListener("click", nextStep);
stage3Button.addEventListener("click", nextStep);
stage4Button.addEventListener("click", nextStep);
stage5Button.addEventListener("click", nextStep);
    
window.addEventListener("online", checkNetwork);
window.addEventListener("offline", checkNetwork);

lockscreen.addEventListener("click", unlock);

document.oncontextmenu = function() {
  return false;
}

// Intervals

setInterval(updateTime, 0);

// Load Code

loadData();

if (localStorage.setup === "true") {
  stage1.style.display = "none";
  lockscreen.style.display = "";
}
