
prompt =    """
            In this scene you'll be doing a Proximity Sensor Test. You'll be given instructions to walk to specific locations within the city.
            When you reach the destination point wait there until you are given further instructions.
            """

prompt2 =   """
            In this scene you'll repeat the steps you did in the previous scene, except here you will make all the avatars walk into the classroom
            """
prompt3 =  """
                                                           Welcome to Deep Learing Game Module!
           Press a to begin when in Scene 1 and b to begin when in Scene 2. Use keys 1 and 2 to switch between Scenes
           
           
           
           """
          
import viz
import vizact
import vizproximity
import viztask
import vizinfo
import vizdlg
import vizshape
import vizconnect
from vizconnect.util import view_collision
import os


viz.phys.enable()

DelayHide0 = vizact.sequence( vizact.waittime(10), vizact.method.visible(False) )
Show0 = vizact.method.visible(True)
instructions0 = vizinfo.InfoPanel(prompt3, align=viz.ALIGN_CENTER_CENTER)
instructions0.runAction(DelayHide0)


viz.setMultiSample(4)
viz.fov(60)
#viz.go(viz.FULLSCREEN)

vizact.onkeydown( '1', viz.MainWindow.setScene, viz.Scene1 )
vizact.onkeydown( '2', viz.MainWindow.setScene, viz.Scene2 )
#Add info panel to display messages to participant

viz.MainView.setPosition([4, 2, 2])
#Set the current position and orientation as point to reset to.
viz.cam.setReset()
#Reset the camera to that point.
vizact.onkeydown('r', viz.cam.reset )

viz.collision(viz.ON)

BirdEyeWindow = viz.addWindow(scene = viz.Scene1)
BirdEyeWindow.fov(60)
BirdEyeView = viz.addView(scene = viz.Scene1)
BirdEyeWindow.setView(BirdEyeView)
BirdEyeView.setPosition([0,25,0])
BirdEyeView.setEuler([0,90,0])

RearWindow = viz.addWindow(scene = viz.Scene1)
RearWindow.fov(60)
RearView = viz.addView(scene = viz.Scene1)
RearWindow.setView(RearView)
RearWindow.setPosition([0,1])

#Make RearView look behind MainView
viewLink = viz.link(viz.MainView,RearView)
viewLink.preEuler([180, 0, 0]) #spin view backwards



piazza = viz.addChild('Assignment2_modified.osgb')


sky = viz.add(viz.ENVIRONMENT_MAP, 'sky.jpg')
skybox = viz.add('skydome.dlc')
skybox.texture(sky)

text3D = viz.addText('Deep Learning Institute',pos=[7,6,31])
text3D.alignment(viz.ALIGN_CENTER_BOTTOM)
text3D.color(viz.BLUE)

timerPanel = vizinfo.InfoPanel('timer: 0', icon=False, align=viz.ALIGN_RIGHT_CENTER)
timerPanel.time = 0

def timer():
    timerPanel.time += 1
    timerPanel.setText('timer: {}'.format(timerPanel.time))
vizact.ontimer(1, timer)
    
    
    
music = viz.addAudio('driv2.mp3', volume=0.075,loop=1)
music.play()


male2 = viz.addAvatar('vcc_male2.cfg')
male2.setPosition ([4, 2, 5])
male2.setEuler([0,0,0])
male2.state(4)

def avatarWalk():  #interactivity element 
    info = viz.pick(1)
    if info.valid and info.object == piazza:
        walk = vizact.walkTo([info.point[0],2,info.point[2]])
        male2.runAction(walk)
        
vizact.onkeydown('3', avatarWalk)

class MyCameraHandler( viz.CameraHandler ):

    def _camMouseDown( self, e ):
        if e.button == viz.MOUSEBUTTON_LEFT:
            #move view down
            e.view.move( [0, -1, 0] )
        elif e.button == viz.MOUSEBUTTON_RIGHT:
            #move view up
            e.view.move( [0, 1, 0] )

    def _camMouseWheel( self, e ):
        if e.dir > 0:
            #wheel rolled forward
            e.view.move( [1, 0, 0] )
        else:
            #wheel rolled backwards
            e.view.move( [-1, 0, 0] )

    def _camUpdate( self, e ):
        #Check keyboard movement
        if viz.key.isDown ('w' ):
            #move forward the amout of time in seconds sence the last call to _camUpdate
            e.view.move( [0, 0, e.elapsed * 10] )
        elif viz.key.isDown ('s' ):
            #move backward the amout of time in seconds sence the last call to _camUpdate
            e.view.move( [0, 0, -e.elapsed * 10] )



#Set camera handler
viz.cam.setHandler( MyCameraHandler() )

#Remove camera handler on spacebar (will revert to built-in camera handler)
vizact.onkeydown( ' ', viz.cam.setHandler, None )
            

male = viz.addAvatar('vcc_male.cfg')
male.setPosition ([5, 2, 5])
male.setEuler([0,0,0])
male.state(14)

def avatarWalk(): #interactivity element 
    info = viz.pick(1)
    if info.valid and info.object == piazza:
        walk = vizact.walkTo([info.point[0],2,info.point[2]])
        male.runAction(walk)
vizact.onkeydown('4', avatarWalk)


female = viz.addAvatar('vcc_female.cfg')
female.setPosition([6,2,5])
female.setEuler([0,0,0])
female.state(14)

def avatarWalk(): #interactivity element 
    info = viz.pick(1)
    if info.valid and info.object == piazza:
        walk = vizact.walkTo([info.point[0],2,info.point[2]])
        female.runAction(walk)

vizact.onkeydown('5', avatarWalk) #interactivity element 

def move():
     info = viz.pick(1)
     if info.valid and info.object == piazza:
        viz.MainView.move([4,2,23])
vizact.onkeydown('m', move)

plant = viz.addChild('plant.osgb')
plant.setPosition([7,2,20])

plant2 = viz.addChild('plant.osgb')
plant2.setPosition([7,2,21])

plant3 = viz.addChild('plant.osgb')
plant3.setPosition([7,2,22])

plant4 = viz.addChild('plant.osgb')
plant4.setPosition([7,2,23])

plant5 = viz.addChild('plant.osgb')
plant5.setPosition([3,2,20])

plant6 = viz.addChild('plant.osgb')
plant6.setPosition([3,2,21])

plant7 = viz.addChild('plant.osgb')
plant7.setPosition([3,2,22])

plant8 = viz.addChild('plant.osgb')
plant8.setPosition([3,2,23])

import random

pigeons = []
for i in range(10):

    #Generate random values for position and orientation
    x = random.randint(0,5)
    z = random.randint(10,25)
    yaw = random.randint(0,360)

    #Load a pigeon
    pigeon = viz.addAvatar('pigeon.cfg')

    #Set position, orientation, and state
    pigeon.setPosition([x,2,z])
    pigeon.setEuler([yaw,0,0])
    pigeon.state(3)

    #Append the pigeon to a list of pigeons
    pigeons.append(pigeon)

############### Sensor Code ########################

#Create sensors for destinations
plantSensor = vizproximity.Sensor(vizproximity.Box([7, 2 ,1],center=[0,1,0]),source=plant)
instituteSensor = vizproximity.Sensor(vizproximity.Box([7, 2, 1],center=[0,1,0]), source = plant4)

#Add main viewpoint as proximity target
target = vizproximity.Target(viz.MainView)

#Create proximity manager
manager = vizproximity.Manager()

#Add destination sensors to manager
manager.addSensor(plantSensor)
manager.addSensor(instituteSensor)

#Add viewpoint target to manager
manager.addTarget(target)

#Toggle debug shapes with keypress
vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)

def instruction():
    instructions = vizinfo.InfoPanel(prompt, align=viz.ALIGN_RIGHT_BOTTOM)
    
    def destinationsTask():

        # Action for hiding/showing text
        DelayHide = vizact.sequence( vizact.waittime(10), vizact.method.visible(False) )
        Show = vizact.method.visible(True)
        yield viztask.waitTime(15)
        instructions.setText("Press 3 to make the male2 avatar walk to the potted plant. Make sure your cursor is pointing towards the entrance . Use key w to move the camera forward, s to move the camera backaward. Press the right mouse key to jump. Roll the mouse wheel to pan left and right")
        instructions.runAction(DelayHide)
        yield vizproximity.waitEnter(plantSensor)
        instructions.runAction(Show)
        instructions.setText("Now, move the camera close to the institute. ")
        instructions.runAction(DelayHide)
        yield vizproximity.waitEnter(instituteSensor)
        instructions.runAction(Show)
        instructions.setText("Repeat the same process with the male avatar using key 4, key 5 for the female avatar or move onto the next scene using key 2. Press a to repeat the instructions.  Press the spacebar to remove the camera handler. Press 0, then right click and s key to return to home view when in Scene 2")
        instructions.runAction(DelayHide)
    viztask.schedule( destinationsTask() )
vizact.onkeydown('a', instruction)

viz.go()

def instruction2():
    instructions2 = vizinfo.InfoPanel(prompt2, align=viz.ALIGN_RIGHT_BOTTOM)
    
    def destinationsTask2():
        # Action for hiding/showing text
        DelayHide2 = vizact.sequence( vizact.waittime(15), vizact.method.visible(False) )
        Show2 = vizact.method.visible(True)
        yield viztask.waitTime(15)
        instructions2.setText("Press 3 to make the male2 avatar walk inside the institute where the door keeps opening and closing. Make sure your cursor is pointing towards the entrance. Use key w to move the camera forward, s to move the camera backaward. Press the right mouse key to jump. Roll the mouse wheel to pan left and right.")
        instructions2.runAction(DelayHide2)
        yield viztask.waitTime(15)
        instructions2.runAction(Show2)
        instructions2.setText("Now, walk inside the classroom where the door keeps opening and closing. Hover the cursor to the entrance of the classroom, while pressing the 3 key ")
        instructions2.runAction(DelayHide2)
        yield viztask.waitTime(15)
        instructions2.runAction(Show2)
        instructions2.setText("Once inside the classroom, repeat the same process with the male avatar using key 4, key 5 for the female avatar. Use key w to move the camera forward, s to move the camera backaward. Roll the mouse wheel to pan left and right. Press the spacebar to remove the camera handler.")
        instructions2.runAction(DelayHide2)
        yield viztask.waitTime(15)
        instructions2.runAction(Show2)
        instructions2.setText("Press the key q to mark the instructor, and press p to get a deep learning definition")
        instructions2.runAction(DelayHide2)
        yield viztask.waitTime(15)
        instructions2.runAction(Show2)
        instructions2.setText("Press the key r to open the modes of instructions dialog box and select the type of mode you wish to learn from (Warning: Make sure your camera is in camera handler mode and is set to pivot mode)")
        yield viztask.waitTime(15)
        instructions2.runAction(DelayHide2)
    viztask.schedule( destinationsTask2() )
vizact.onkeydown('b', instruction2)

#Add a model to the new scene
school = viz.addChild('Buildings.osgb', scene=viz.Scene2)
school.setPosition([0,2,0], viz.REL_LOCAL)


ground = viz.addChild('ground.osgb', scene=viz.Scene2)
ground.collidePlane()
ground.setPosition([0,1.85,0])

sky = viz.add(viz.ENVIRONMENT_MAP, 'sky.jpg', scene=viz.Scene2)
skybox = viz.add('skydome.dlc',scene=viz.Scene2)
skybox.texture(sky)

text3DCopy = viz.addText('Welcome To Deep Learning Institute',pos=[0,5,12], scene=viz.Scene2)
text3DCopy.alignment(viz.ALIGN_CENTER_BOTTOM)
text3DCopy.color(viz.BLUE)

#Add the path.
path = viz.addAnimationPath()

#Add control points to the path, along with their time stamp.
path.addControlPoint(0,pos=(2,2,5),euler=(90,0,0),scale=(2,2,2))
path.addControlPoint(3,pos=(-2,2,6),euler=(0,90,0),scale=(.5,.5,.5))

#Loop the path in a swinging fashion (point A to point B to point A, etc.).
path.setLoopMode(viz.SWING)

#Add a model.
door = viz.addChild('beachball.osgb', scene = viz.Scene2)

#Link the model to a path.
link = viz.link(path,door) #interactivity element

#Play the path.
path.play()

male2Copy = male2.copy(scene=viz.Scene2)
male2Copy.setPosition ([4, 2, 5])
male2Copy.setEuler([0,0,0])
male2Copy.state(4)


def avatarWalk(): #interactivity element
    info = viz.pick(1)
    if info.valid and info.object == school:
        walk = vizact.walkTo([4,2,8.5])
        walk2 = vizact.walkTo([1.5,2,8.5])
        walk3 = vizact.walkTo([1.5,2,14])
        walk4 = vizact.walkTo([-2,2,14])
        walk5 = vizact.walkTo([-2,2,18])
        walk6 = vizact.walkTo([-8,2,18])
        male2Copy.addAction(walk)
        male2Copy.addAction(walk2)
        male2Copy.addAction(walk3)
        male2Copy.addAction(walk4)
        male2Copy.addAction(walk5)
        male2Copy.addAction(walk6)
        
        
vizact.onkeydown('3', avatarWalk)

maleCopy = male.copy(scene=viz.Scene2)
maleCopy.setPosition ([3, 2, 5])
maleCopy.setEuler([0,0,0])
maleCopy.state(14)

def avatarWalk():
    info = viz.pick(1)
    if info.valid and info.object == school:
        walk = vizact.walkTo([3,2,8.5])
        walk2 = vizact.walkTo([1.5,2,8.5])
        walk3 = vizact.walkTo([1.5,2,14])
        walk4 = vizact.walkTo([-2,2,14])
        walk5 = vizact.walkTo([-2,2,18])
        walk6 = vizact.walkTo([-8,2,19])
        maleCopy.addAction(walk)
        maleCopy.addAction(walk2)
        maleCopy.addAction(walk3)
        maleCopy.addAction(walk4)
        maleCopy.addAction(walk5)
        maleCopy.addAction(walk6)
        
vizact.onkeydown('4', avatarWalk)


femaleCopy = female.copy(scene=viz.Scene2)
femaleCopy.setPosition ([5, 2, 5])
femaleCopy.setEuler([0,0,0])
femaleCopy.state(14)

def avatarWalk():
    info = viz.pick(1)
    if info.valid and info.object == school:
        walk = vizact.walkTo([5,2,8.5])
        walk2 = vizact.walkTo([1.5,2,8.5])
        walk3 = vizact.walkTo([1.5,2,14])
        walk4 = vizact.walkTo([-2,2,14])
        walk5 = vizact.walkTo([-2,2,18])
        walk6 = vizact.walkTo([-8,2,20])
        femaleCopy.addAction(walk)
        femaleCopy.addAction(walk2)
        femaleCopy.addAction(walk3)
        femaleCopy.addAction(walk4)
        femaleCopy.addAction(walk5)
        femaleCopy.addAction(walk6)
        
        
vizact.onkeydown('5', avatarWalk)

def onCollideBegin(e):
    if e.obj1 == male2Copy:
        if e.obj2 == school:
            school.color(viz.RED)
            vizact.ontimer2(.1,0,school.color,viz.BLUE)
viz.callback(viz.COLLIDE_BEGIN_EVENT,onCollideBegin)


plant = plant.copy(scene=viz.Scene2)
plant.collidePlane()
plant.setPosition([2,2,10])

plant2 = plant2.copy(scene=viz.Scene2)
plant.collidePlane()
plant2.setPosition([2,2,8])

plant3 = plant3.copy(scene=viz.Scene2)
plant.collidePlane()
plant3.setPosition([-2,2,10])

plant4 = plant4.copy(scene=viz.Scene2)
plant.collidePlane()
plant4.setPosition([-2,2,8])

chair= viz.addChild('chair.osgb', scene = viz.Scene2)
chair.setPosition([-5,2.10, 20])
chair.setEuler([-90, 0, 0])

chair2= viz.addChild('chair.osgb', scene = viz.Scene2)
chair2.setPosition([-6,2.10, 23])
chair2.setEuler([-90, 0, 0])

avatar1 = viz.addAvatar('vcc_male2.cfg',pos=[7 ,1.80,11],euler=[180,0,0],scale=[0.95,0.95,0.95], scene=viz.Scene2)
avatar2 = avatar1.copy(pos=[6,1.80,11],euler=[180,0,0], scene=viz.Scene2)
avatar3 = avatar1.copy(pos=[-2,2,5.6],euler=[180,0,0], scene=viz.Scene2)
avatar1.state(6)
avatar2.state(6)
avatar3.state(5)

avatar4 = viz.addAvatar('vcc_male.cfg',pos=[-2 ,2.10, 21],euler=[-60,0,0],scale=[0.95,0.95,0.95], scene=viz.Scene2)

def talk():
    speech = viz.addAudio('DeepLearning.mp3', volume=0.60,loop=0)
    speech.play()
vizact.onkeydown('p', talk)

avatar5 = avatar1.copy(pos=[-5,1.90, 20],euler=[90,0,0], scene=viz.Scene2)
avatar6 = avatar1.copy(pos=[-6,1.90, 23],euler=[90,0,0], scene=viz.Scene2)
avatar4.state(14)
avatar5.state(6)
avatar6.state(6)

deepLearning = viz.addTexQuad(texture=viz.addTexture('DeepLearning.gif'), scale=(7.5,2,2), pos=(-1.5, 3.75, 21.25), euler=(90,0,0), scene=viz.Scene2)
deepLearning2 = viz.addTexQuad(texture=viz.addTexture('DeepLearning2.jpeg'), scale=(3.0,2,2), pos=(-9.75, 3.75, 25), euler=(0,0,0), scene=viz.Scene2)
deepLearning3 = viz.addTexQuad(texture=viz.addTexture('DeepLearning3.jpg'), scale=(3.0,2,2), pos=(-6.5, 3.75, 25), euler=(0,0,0), scene=viz.Scene2)
deepLearning4 = viz.addTexQuad(texture=viz.addTexture('DeepLearning4.jpg'), scale=(3.0,2,2), pos=(-3.25, 3.75, 25), euler=(0,0,0), scene=viz.Scene2)

#Set the animation speed and mode

modePanel = vizinfo.InfoPanel('', title='Rotate Mode', align=viz.ALIGN_CENTER_TOP)
none = modePanel.addLabelItem('None',viz.addRadioButton('RotateMode'))
pivot = modePanel.addLabelItem('Pivot',viz.addRadioButton('RotateMode'))
none.set(True)

#Set the animation speed and mode
SPEED = 2.5
MODE = viz.SPEED
ROTATE_MODE = viz.NO_ROTATE

def SetRotateMode(mode):
	global ROTATE_MODE
	ROTATE_MODE = mode

def AnimateView(pos):
	action = vizact.goto(pos,SPEED,MODE,pivot=(90, 0, 0),rotate_mode=ROTATE_MODE)
	viz.MainView.runAction(action)
#Setup keyboard events
vizact.onkeydown('0',AnimateView,[6, 2, 3])
vizact.onkeydown('6',AnimateView,[-8,3.5,21])
vizact.onkeydown('7',AnimateView,[-8,3,21])
vizact.onkeydown('8',AnimateView,[-6,3,21])
vizact.onkeydown('9',AnimateView,[-4,3,21])

#Setup button click events
vizact.onbuttondown(none,SetRotateMode,viz.NO_ROTATE)		#The viewpoint will not rotate while it's  moving

vizact.onbuttondown(pivot,SetRotateMode,viz.PIVOT_ROTATE)	#The viewpoint will look at the pivot point while it's moving

#Start off by moving to the first location
AnimateView([4, 2, 3])

viz.clearcolor(viz.SLATE)

arrow = viz.addChild('arrow.wrl', scene = viz.Scene2)
arrow.setScale([0.1,0.1,0.1])
arrow.visible(viz.OFF)

arrow.disable(viz.PICKING)

def pickAvatar():
	object = viz.pick()
	if object.valid():
		arrow.setPosition([-2, 4 ,21])
		arrow.visible(viz.ON)

vizact.onkeydown('q', pickAvatar)


def mode():
    
    DelayHide3 = vizact.sequence( vizact.waittime(15), vizact.method.visible(False) )
    Show3 = vizact.method.visible(True)
    
    critical_question = viz.addText('Mode of Instruction: ',viz.SCREEN, scene = viz.Scene2)
    critical_question.color(1,0,0)
    tut = viz.addText('Tutorial Mode',viz.SCREEN, scene = viz.Scene2)
    tut.color(1,0,0)
    inter = viz.addText('Interactive Mode',viz.SCREEN, scene = viz.Scene2)
    inter.color(1,0,0)
    feed =  viz.addText('Feedback Mode',viz.SCREEN, scene = viz.Scene2)
    feed.color(1,0,0)
    
    critical_question.alignment(viz.ALIGN_CENTER_CENTER)
    critical_question.setPosition([.5,.65, 0])
    critical_question.runAction(DelayHide3)


    tut.alignment(viz.ALIGN_LEFT_CENTER)
    tut.setPosition([.25,.45, 0])
    tut.runAction(DelayHide3)


    inter.alignment(viz.ALIGN_LEFT_CENTER)
    inter.setPosition([.25,.35, 0])
    inter.runAction(DelayHide3)
    
    feed.alignment(viz.ALIGN_LEFT_CENTER)
    feed.setPosition([.25,.25, 0])
    feed.runAction(DelayHide3)

    tut_button = viz.addButton(scene = viz.Scene2)
    tut_button.setPosition([.20,.45,0])
    tut_button.runAction(DelayHide3)
    
    
    inter_button = viz.addButton(scene = viz.Scene2)
    inter_button.setPosition([.20,.35, 0])
    inter_button.runAction(DelayHide3)
    
    feed_button = viz.addButton(scene = viz.Scene2)
    feed_button.setPosition([.20,.25, 0])
    feed_button.runAction(DelayHide3)

    def onbutton(obj,state):
        
        if obj == tut_button:
            r = vizinfo.InfoPanel('Press Keys 7 through 9 to view png examples of deep learning module while in none mode.', align=viz.ALIGN_LEFT_CENTER)
            r.runAction(DelayHide3)
        if obj == inter_button:
            k = vizinfo.InfoPanel('Press Key 6 to view an gif example of a deep learning neural network while in pivot mode. ', align=viz.ALIGN_LEFT_BOTTOM)
            k.runAction(DelayHide3)
        if obj == feed_button:
            os.startfile(r"C:\Users\syeda\OneDrive - Bowie State\COSC 729\Assignments\Assignment 3\mcq.exe")
    viz.callback(viz.BUTTON_EVENT,onbutton)

vizact.onkeydown('r', mode)       

