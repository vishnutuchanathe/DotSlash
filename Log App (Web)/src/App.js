import logo from './logo.svg';
import './App.css';
import {storage} from './firebase';
import React,{useEffect, useState} from 'react';
import Nav from './Nav';
import { getStorage, ref, getMetadata } from "firebase/storage";

function App() {
  const [imageTab, setImageTab] = useState([]);
  const [imageDate, setImageDate] = useState([]);

  useEffect(() => {
    storage
      .ref('/')
      .listAll()
      .then(function(result) {
          result.items.forEach(function(imageRef) {
            getMetadata(imageRef)
            .then((metadata) => {
              imageDate.push(metadata.timeCreated);
                  setImageDate(imageDate);
              
            })
            .catch((error) => {
            });
              imageRef.getDownloadURL().then(function(url) {
                  imageTab.push(url);
                  setImageTab(imageTab);
              }).catch(function(error) {
              });
          });
      })
      .catch((e) => console.log('Errors while downloading => ', e));
  }, []);
  return (
    <div className="App">
    <Nav/>
    <div className="log">
    <table className='table'>
    <thead className='thead-dark'>
    <tr>
    <th scope="col">Time</th>
    <th scope="col">Capture</th>
    </tr>
    </thead>
    {imageTab.map((i,ind)=> (
                    <tr>
                        <td>{imageDate[ind]}</td>
                        <td><img style={{height: 200, width: 200}} src={i} /></td>
                    </tr>
                ))}
    </table>
    </div>
    
    </div>
  );
}

export default App;
