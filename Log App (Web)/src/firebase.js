import firebase from 'firebase/compat/app';
import 'firebase/compat/storage';

const config = {
    apiKey: "",
    authDomain: "",
    projectId: "",
    storageBucket: "",
    messagingSenderId: "",
    appId: ""
}
firebase.initializeApp(config);
const storage = firebase.storage();
export {storage};