// Web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCmE7pclF-elhD_BybfUi5rbnoLopaCjos",
    authDomain: "cardservices-c108a.firebaseapp.com",
    projectId: "cardservices-c108a",
    storageBucket: "cardservices-c108a.appspot.com",
    messagingSenderId: "581581917182",
    appId: "1:581581917182:web:4341531479eebf480c8eaf",
    measurementId: "G-4PLDD26ZBG"
  };
  
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  // Check to see if Firebase Analytics is supported in the current environment

  if (firebase.analytics && firebase.analytics.isSupported()) {
    firebase.analytics();
  }
  

  // Initialize Firebase Authentication UI
  const ui = new firebaseui.auth.AuthUI(firebase.auth());
  
  // FirebaseUI config object
  //const uiConfig = {
      // Your UI Config
  //};
  
  // The start method will wait until the DOM is loaded.
  //ui.start('#firebaseui-auth-container', uiConfig);
  
  // Check to see if Firebase Analytics is supported in the current environment
  if (firebase.analytics.isSupported()) {
      const analytics = firebase.analytics();
  }
  