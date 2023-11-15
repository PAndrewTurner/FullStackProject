const firebaseConfig = {
    // Your Firebase configuration here
  };
  
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  
  const uiConfig = {
    callbacks: {
      signInSuccessWithAuthResult: function (authResult, redirectUrl) {
        // Redirect to '/main/dashboard/' after successful login
        return true;
      },
      uiShown: function () {
        // The widget is rendered.
        // Hide the loader or perform any other UI-related tasks.
      },
    },
    signInFlow: 'popup',
    signInSuccessUrl: '/main/dashboard/'
    signInOptions: [
      // List of OAuth providers supported.
      firebase.auth.GoogleAuthProvider.PROVIDER_ID,
      firebase.auth.EmailAuthProvider.PROVIDER_ID,
    ],
  };
  
  // Initialize the FirebaseUI Widget using Firebase
  const ui = new firebaseui.auth.AuthUI(firebase.auth());
  
  // Start the FirebaseUI Widget
  ui.start('#firebaseui-auth-container', uiConfig);
  const firebaseConfig = {
    // Your Firebase configuration here
  };
  
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  
  const uiConfig = {
    callbacks: {
      signInSuccessWithAuthResult: function (authResult, redirectUrl) {
        // Redirect to '/main/dashboard/' after successful login
        window.location.href = '/main/dashboard/';
        return false; // Return false to prevent automatic redirect
      },
      uiShown: function () {
        // The widget is rendered.
        // Hide the loader or perform any other UI-related tasks.
      },
    },
    signInFlow: 'popup',
    signInSuccessUrl: false, // Disable automatic redirect
    signInOptions: [
      // List of OAuth providers supported.
      firebase.auth.GoogleAuthProvider.PROVIDER_ID,
      firebase.auth.EmailAuthProvider.PROVIDER_ID,
    ],
  };
  
  // Initialize the FirebaseUI Widget using Firebase
  const ui = new firebaseui.auth.AuthUI(firebase.auth());
  
  // Start the FirebaseUI Widget
  ui.start('#firebaseui-auth-container', uiConfig);
    