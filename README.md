# DotSlash

Animal Intrusion Detection System (Elephant) - A solution to crop damage

<h2> Problem Statement </h2>

<p>
  
Animals like Elephants often get out otheir habitat and enter village borders during migration or in search of food, it destroys human property especially <b>crops and farm lands</b>. We have thus came up with the idea of an animal intrusion detection stystem (Elephants) to detect elephants near the village border and caution the farmers of the sighting. This gives them the needed buffer time to take the appropriate action.
  
</p>


<p>

The repository includes:

  <ul>
  <li>PPT</li>
  <li>Project Code</li>
  <li>Project Demo</li>
</ul>
  
</p>


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


<h2> Project Setup </h2>
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

<p>
  
  <h4> 1. Requirements </h4>
  
  <p>
  
  The required python  packages are mentioned  in the requirements.txt file.
  
</p>
  
  <h4> 2. Project Setup </h4>
  
  <p>
  
  Download the following the repository and follow the intsallation instructions given in the readme file

  <a href="https://github.com/matterport/Mask_RCNN">Mask RCNN Repository</a>
  
</p>

<h4> 3. Main Code </h4>
  
  <p>
  
 Create a folder Inside the Mask RCNN Master, and give the name of your choice. Download the repository content in this new folder
  
</p>
  

<h4> 4.Code Excution </h4>
  
  <p>
  
Execute the python file, python video_demo0.py
  
</p>



</p>


<h2> Modules </h2>

In the animal intrusion detection system, we have three main modules and it is explained below

<ul>
  <li>Capture Module  </li>
  <li>Detect Module </li>
   <li>Alert Module </li>
</ul>
  
  
  <h4> Capture Module </h4>
  
  
  <p>
  
   On clicking on the start button in the front end interface, all the CCTVs linked to
the software will get activated  < <b> (In our case we have used web cameras for capturing the animals ) </b>. They will simultaneously be continuously
capturing scenes from the environment that they are placed in which may or may
not capture any elephant approaching the boundaries, assuming the cameras are
placed in the boundary perimeter of the forest region.
  
  </p>
  
  
  <h> Detect Module </h4>
  
  <p>
  The matterport (Mask RCNN) model loaded with pretrained ms coco weights successfully recognizes the elephants that are captured in the frame that is capable
  of recognizing 80 classes and elephant is one of them. Opencv is used for capturing frames or images of environment through an optical
system. The captured frames are then checked for elephant using the model’s built in function “detect”. The detect function provides us with bounding boxes, masks, class id and other information from the image. The result is checked for the class labels found in the frame, if it contains elephant the image is masked and given as output. ● On detection of the elephant by the application the alert module will be triggered.
  
  </p>
  
  
  <h4> Alert Module </h4>
  
  <p>
  
Once the elephant is detected the twilio api is called to initiate a call to the respective authority, the call plays a recorded message which was passed to the
api function in the form of a cloud hosted xml file. THe program also throws an alert box on the screen to notify the front user.
  
  </p>
  
  

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  
  

