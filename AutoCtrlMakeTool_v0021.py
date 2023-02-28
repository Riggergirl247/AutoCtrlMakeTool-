#######################################################################################
# Auto Ctrl Tool
# Version: 2.10
# by Aashi Shukla
#--------------------------------------------------------------------------------------
# This tool has almost all the features you need for Control Creation and modification.
# It was especially build keeping in mind, the need to finish  small props and Fk Chain 
# rigs in the least number of clicks possible. The idea is to  finish the work  quickly 
# and efficiently. It consists of three main tabs: Main, Utility and Help.
#
# In the Main Tab, you can specify the radius, choose the color, shape and Constraining
# options and it will build the rig for you. If you need  seperate groups like Mesh_Grp,
# Jnt_Grp and Ctrl_Grp, then tick on Rig  Groups, give it a  name and click on  "Build".
# Please note that  if you click on the  "Create"  button instead, it will not Build the
# rig groups. So, if you need the Rig Groups  and Global Ctrl, just click on the "Build"
# button.
#
# The Global Ctrl will provide you with 5 Custom Attributes: Global Scale, Mesh Display,
# Mesh Visibility, Ctrl  Visibility and  Joint Visibility. By default, you will get all
# 5 of them; connected properly with their respective nodes but you also get the option
# to choose all the Attributes you don't need. 
# 
# The Utility Tab contains a bunch of Renaming and Joint tools, that will prove to be 
# helpful in your rig creation and speed up your workflow.
# 
# The Help Tab, as the name suggests contains all the help you need regarding this tool.
# You can report the bugs on: aashi41207@gmail.com 
#--------------------------------------------------------------------------------------
# To run this script, paste this file as it is, in your Maya Scripts directory:
# C:\Users\UserName\Documents\maya\2020\scripts
# and then paste the following code in your Script Editor:
#
# import AutoCtrlMakeTool_v0021
# import imp
# imp.reload(AutoCtrlMakeTool_v0021)
# AutoCtrlMakeTool_v0021.GUI()
# and Run!
#-------------------------------------------------------------------------------------
# (Maya 2023 and all previous versions supported)
# Rest, I hope that this tool proves to be a useful asset in your rigging mania!
########################################################################################


from functools import partial
import maya.cmds as cmds


def GUI():
	# Kill the window if already exists
	if cmds.window('Shape_Create_UI', exists=True):
		cmds.deleteUI( 'Shape_Create_UI')
	
	# Create a new window
	Win = cmds.window('Shape_Create_UI', t='AutoCtrlMakeTool', wh=(420,450), sizeable= False, mnb=1,mxb=0)
	# Parent Layout
	tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
	# Defining main tab
	main_tab = cmds.formLayout(p=tabs)
	cmds.formLayout(main_tab, edit=True)
	# Defining others tab
	others_tab = cmds.formLayout(p=tabs)
	cmds.formLayout(others_tab, edit=True)
	# Defining Help tab
	helper_tab = cmds.formLayout(p=tabs)
	cmds.formLayout(helper_tab, edit=True)
	# naming tabs
	cmds.tabLayout(tabs, edit=True, tabLabel= ((main_tab, "Main"),(others_tab,"Utility"),(helper_tab,"Help")))
	Main_Layout_01 = cmds.rowColumnLayout(adj=1,p=main_tab)
	cmds.columnLayout(adj=1, columnAlign = 'center')
	cmds.text( l = 'Make_Ctrl by @Aashi Shukla' )
	cmds.separator(h=10, st='in')
	cmds.setParent('..')
		
	# Takes the radius and makes a shape Ctrl that is constrained with the joint
	cmds.rowColumnLayout( nr=1 )
	cmds.separator(w=10, st='none')
	cmds.text( l='Radius: ')
	Radius = cmds.floatField(value=1.0)
	cmds.optionMenuGrp('Ctrl_Sel_Menu', label='Ctrl Shape:')
	cmds.menuItem(label='cube')
	cmds.menuItem(label='circle')
	cmds.menuItem(label='square')
	cmds.menuItem(label='triangle')
	cmds.menuItem(label='Hexagon')
	cmds.menuItem(label='COG')
	cmds.menuItem(label='Plus')
	cmds.menuItem(label='Arrow')
	cmds.menuItem(label='locator')
	cmds.setParent('..')
	
	# Takes the color of ctrls
	cmds.rowColumnLayout( nr=1 )
	cmds.separator( w= 71,st='none' )
	cmds.button( l="", bgc = (0.631, 0.631, .631), w=7 )
	cmds.button( l="", bgc = (0.467, 0.6467, .631), w=7 )
	cmds.button( l="", bgc = (0, 0, 0), w=7 )
	cmds.button( l="", bgc = (0.247, 0.247, .247), w=7 )
	cmds.button( l="", bgc = (0.498, 0.498, .498), w=7 )
	cmds.button( l="", bgc = (0.608, 0.0, .157), w=7 )
	cmds.button( l="", bgc = (0 ,0.016 ,0.373), w=7 )
	cmds.button( l="", bgc = (0 ,0 ,1), w=7 )
	cmds.button( l="", bgc = (0 ,0.275 ,0.094), w=7 )
	cmds.button( l="", bgc = (0.145, 0, 0.263), w=7 )
	cmds.button( l="", bgc = (0.78, 0, 0.78), w=7 )
	cmds.button( l="", bgc = (0.537, 0.278, 0.2), w=7 )
	cmds.button( l="", bgc = (0.243, 0.133, 0.122), w=7 )
	cmds.button( l="", bgc = (0.6, 0.145, 0), w=7 )
	cmds.button( l="", bgc = (1, 0, 0), w=7 )
	cmds.button( l="", bgc = (0, 1, 0), w=7 )
	cmds.button( l="", bgc = (0, 0.255, 0.6), w=7 )
	cmds.button( l="", bgc = (1, 1, 1), w=7 )
	cmds.button( l="", bgc = (1, 1, 0), w=7 )
	cmds.button( l="", bgc = (0.388 , 0.863, 1), w=7 )
	cmds.button( l="", bgc = (0.263, 1, 0.635), w=7 )
	cmds.button( l="", bgc = (1, 0.686, 0.686), w=7 )
	cmds.button( l="", bgc = (0.89, 0.675, 0.475), w=7 )
	cmds.button( l="", bgc = (1, 1, 0.384), w=7 )
	cmds.button( l="", bgc = (0.0, 0.6, 0.325), w=7 )
	cmds.button( l="", bgc = (0.627, 0.412, 0.188), w=7 )
	cmds.button( l="", bgc = (0.62, 0.627, 0.188 ), w=7 )
	cmds.button( l="", bgc = (0.408, 0.627, 0.188 ), w=7 )
	cmds.button( l="", bgc = (0.188, 0.627, 0.365  ), w=7 )
	cmds.button( l="", bgc = (0.188, 0.627, 0.627 ), w=7 )
	cmds.button( l="", bgc = (0.188, 0.404, 0.627), w=7 )
	cmds.button( l="", bgc = (0.435, 0.188, 0.627), w=7 )
	cmds.button( l="", bgc = (0.631, 0.188, 0.412), w=7 )
	cmds.setParent('..')
	cmds.separator( st='none')
	
	# Input of colors
	cmds.rowColumnLayout( nr=1 )
	Color= cmds.colorIndexSliderGrp( min=1 , max=32, value=19, w=300 )
	cmds.button( l='Color', w=100, bgc=(0.257,0,0.257), c= lambda x:Ctrl_Color_Tool(Color) )
	cmds.setParent('..')
	cmds.separator(st='none', h=10)
	
	# CONSTRAINING options: Parent and Scale constraint via Checkboxes
	cmds.separator(h=10, st='in')
	cmds.rowColumnLayout( nr=1 )
	cmds.separator( w=20, st='none')
	cmds.text( l="Constrains: " )
	cmds.separator( w=20, st='none')
	PC=cmds.checkBox( l = 'Parent Constraint', value=True)
	cmds.separator( w=20, st='none')
	SC=cmds.checkBox( l = 'Scale Constraint', value=True )
	cmds.setParent('..')
	
	# Joint Provided?
	cmds.separator(h=10, st='in')
	cmds.rowColumnLayout( nr=1 )
	cmds.separator( w=20, st='none')
	Jnt_Prvd = cmds.checkBox( l ='Joint Provided', al='center')
	cmds.separator(w=50, st='none')
	FK_Chain = cmds.checkBox( l ='FK Chain', enable=False)
	cmds.separator(w=50, st='none')
	Make_Ctrl_Button = cmds.button('Make_Ctrl', l='Create', w=125, enable=False, 
	                                   c=lambda x:Make_C(Radius, Color, FK_Chain, PC, SC))
	cmds.setParent('..')

	# Pivot Position
	cmds.separator(h=10, st='in')
	cmds.rowColumnLayout( nr=1 )
	cmds.separator( w=20, st='none')
	Joint_Pos_Text = cmds.text( l = "Joint Position: ")
	cmds.separator( w=40, st='none')
	cmds.radioCollection(nci=2)
	ps_01 = cmds.radioButton( l = 'Center', select=True )
	cmds.separator( w=20, st='none')
	ps_02 = cmds.radioButton( l = 'Pivot' )
	cmds.separator( w=20, st='none')
	cmds.setParent('..')
	
	# Add Skin Cluster or not:
	cmds.separator(h=10, st='in')
	cmds.rowColumnLayout( nr=1 )
	cmds.separator( w=20, st='none')
	Add_Skin_Cluster_Text = cmds.text( l = "Add Skin Cluster: ")
	cmds.separator( w=25, st='none')
	cmds.radioCollection(nci=2)
	sk_01 = cmds.radioButton( l = 'Yes', select=True )
	cmds.separator( w=39, st='none')
	sk_02 = cmds.radioButton( l = 'No' )
	cmds.separator( w=20, st='none')
	cmds.setParent('..')
	
	
	# Make a separate Rig Group:
	cmds.separator(h=10, st='in')
	cmds.rowColumnLayout( nr=1, co= ([1,"both", 20],[2,"left",20],[3,"both",10]))
	Make_Grp = cmds.checkBox( l ='Make Rig Groups', al='center')
	Rig_Name_Text = cmds.text(l= 'Rig Name : ', enable=False)
	Rig_Name = cmds.textField(w=160, enable=False)
	cmds.setParent('..')
	
	# Add Global Ctrl:
	cmds.separator(h=10, st='in')
	cmds.rowColumnLayout( nr=1 )
	cmds.separator( w=20, st='none')
	Add_Global_Text = cmds.text( l = "Add Global Ctrl: ", enable=False)
	cmds.separator( w=32, st='none')
	cmds.radioCollection(nci=2)
	gb_01 = cmds.radioButton( l = 'Yes', enable=False )
	cmds.separator( w=37, st='none')
	gb_02 = cmds.radioButton( l = 'No', select=True, enable=False )
	cmds.separator( w=20, st='none')
	cmds.setParent('..')
	
	# Global Attributes:
	cmds.separator(h=10, st='in')
	cmds.rowColumnLayout( nr=1 )
	cmds.separator( w=20, st='none')
	Global_Attr_Text = cmds.text( l="Global Attributes: ", enable=False )
	cmds.setParent('..')
	cmds.separator( w=20, st='none')
	# Save Attribute IDs:
	cmds.rowColumnLayout( nc=6 )
	cmds.separator( w=20, st='none')
	Attr_01=cmds.checkBox( l = 'Global Scale', value=True, enable=False )
	cmds.separator( w=20, st='none')
	Attr_02=cmds.checkBox( l = 'Mesh Display', value=True, enable=False )
	cmds.separator( w=20, st='none')
	Attr_03=cmds.checkBox( l = 'Mesh Vis', value=True, enable=False )
	cmds.separator( w=20, st='none')
	Attr_04=cmds.checkBox( l = 'Ctrl Vis', value=True, enable=False )
	cmds.separator( w=20, st='none')
	Attr_05=cmds.checkBox( l = 'Joint VIS', value=True, enable=False )
	cmds.setParent('..')
	
	# Create the push button
	cmds.separator(st='in', h=10)
	cmds.button(l='Build', h=50, c =lambda x:Create(Radius,Color,Jnt_Prvd,FK_Chain, ps_01,ps_02,sk_01,PC,SC,
	                                               Make_Grp,Rig_Name,gb_01,Attr_01,Attr_02,Attr_03,Attr_04,Attr_05))
	cmds.separator(st='out', h=10)
	
	# Disable Pivot Position, Add Skin Cluster and Make Groups if the joints are already provided:
	cmds.checkBox(Jnt_Prvd, e=1, onc = partial( Joint_Provided_Switch, FK_Chain, Make_Ctrl_Button, Joint_Pos_Text, Add_Skin_Cluster_Text, ps_01,ps_02,sk_01,sk_02, True))
	cmds.checkBox(Jnt_Prvd, e=1, ofc = partial( Joint_Provided_Switch, FK_Chain, Make_Ctrl_Button, Joint_Pos_Text, Add_Skin_Cluster_Text, ps_01,ps_02,sk_01,sk_02, False))
	                                           
	# Disable Add Global, Rig Name and add_Attr if RIG Groups are not made:
	cmds.checkBox( Make_Grp, e=1,  onc= partial(Make_Rig_Group, Add_Global_Text, Rig_Name_Text, Rig_Name, gb_01, gb_02, True))
	cmds.checkBox( Make_Grp, e=1,  ofc= partial(Make_Rig_Group, Add_Global_Text, Rig_Name_Text, Rig_Name, gb_01, gb_02, False))
	
	# Disable Global Attributes if Make Global is not selected
	cmds.radioButton(gb_02, e=1, onc= partial( Lock_Global_Attr_Switch, Global_Attr_Text, Attr_01,Attr_02,Attr_03,Attr_04,Attr_05, True))
	cmds.radioButton(gb_02, e=1, ofc= partial( Lock_Global_Attr_Switch, Global_Attr_Text, Attr_01,Attr_02,Attr_03,Attr_04,Attr_05, False))
	
	
	# ======================================================================================
	################### OTHERS SECTION #####################################################
	# main layout
	clm=cmds.columnLayout(p=others_tab, adj=True)
	cmds.rowColumnLayout(nc=4)
	cmds.separator(w=10, st='none')
	cmds.button(w=360, l='Joint Chain', c=lambda x:Make_Parent_Chain())
	cmds.separator(w=15, st='none')
	cmds.button(w=15, l='?', c=lambda x:Parent_Chain_Exp() )
	cmds.setParent(clm)
	cmds.separator(st='in', h=10)
	#####_____________________________________
	cmds.rowColumnLayout(nc=4)
	cmds.separator(w=10, st='none')
	cmds.button(w=360, l='Match Orient', c=lambda x:Match_Orient())
	cmds.separator(w=15, st='none')
	cmds.button(w=15, l='?', c=lambda x:Match_Orient_Exp())
	cmds.setParent(clm)
	cmds.separator(st='in', h=10)
	# 2nd Layout for Shape Change____________________
	cmds.rowColumnLayout(nc=2, co=([1,'both', 5],[2,'both',5]), p = clm)
	cmds.button(l='Joint Place : Center', w=190, c=lambda x:Joint_Place_Center())
	cmds.button(l='Joint Place : Pivot', w=190,  c=lambda x:Joint_Place_Pivot())
	cmds.setParent(clm)
	cmds.separator(st='in', h=10)
	######___________________________________________
	cmds.rowColumnLayout(nc=2,adj=1, p = clm)
	shape_change = cmds.textField(editable=False)
	cmds.button(l='Load', w=100, c=lambda x:Load_Shape(shape_change))
	cmds.optionMenuGrp('Ctrl_Change_Menu',cal=(1,'right'), ad2=2, label='Controller Change Shape : ')
	cmds.menuItem(label='cube')
	cmds.menuItem(label='circle')
	cmds.menuItem(label='square')
	cmds.menuItem(label='triangle')
	cmds.menuItem(label='Hexagon')
	cmds.menuItem(label='Plus')
	cmds.menuItem(label='Arrow')
	cmds.menuItem(label='locator')
	cmds.button(l='Shape Change', w=100, bgc=(0.257,0,0.257) , c=lambda x:Change_Shape(Radius,Color))
	cmds.setParent(clm)
	cmds.separator(st='in', h=10)
	#####__________________________________
	cmds.rowColumnLayout(nc=5, p=clm)
	Prefix = cmds.textField(tx='prefix')
	Padding = cmds.intField(v=1)
	Suffix = cmds.textField(tx='suffix')
	cmds.separator(w=10, st='none')
	cmds.button(l='Rename', w=100, c=lambda x:Rename_Tool(Prefix, Padding, Suffix))
	cmds.setParent('..')
	cmds.separator(h=5, st='none')
	#####_________________________________
	cmds.rowColumnLayout(nc=5, p=clm)
	cmds.separator(w=10, st='none')
	cmds.button( w=150, l='Remove First Character-->', c = Remove_FC )
	cmds.separator(w=10, st='none')
	cmds.button( w=150,  l='<--Remove Last Character', c = Remove_LC )
	cmds.separator(w=10, st='none')
	#####____________________________________
	cmds.setParent(clm)
	cmds.separator(h=5, st='none')
	cmds.rowColumnLayout(nc=7, columnOffset= ([1,"both",3],[2,"both",3],[3,"both",3],
	                                  [4,"both",3],[5,"both",3], [6,"both",3],[7,"both",3]), p=clm)
	cmds.text(l='Add Suffix..')
	cmds.button(l='Jnt', w=50, bgc=(0.257,0,0.257), c= suf_Jnt)
	cmds.button(l='Geo', w=50, bgc=(0.257,0,0.257), c= suf_Geo)
	cmds.button(l='Grp', w=50, bgc=(0.257,0,0.257), c= suf_Grp)
	cmds.button(l='Ctrl', w=50, bgc=(0.257,0,0.257), c= suf_Ctrl)
	cmds.button(l='CON', w=50, bgc=(0.257,0,0.257), c= suf_CON)
	cmds.button(l='OFF', w=50, bgc=(0.257,0,0.257), c= suf_OFF)
	####_______________________________________
	cmds.setParent(clm)
	cmds.separator(h=5, st='none')
	cmds.rowColumnLayout(nc=3, columnOffset= ([1,"both",3],[2,"both",3],[3,"both",3]), p=clm)
	cmds.text(l='Add Custom Prefix...')
	Custom_Prefix = cmds.textField(w=150, text='custom_')
	cmds.button(l='Add',w=100, c=lambda x:Add_Custom_Prefix(Custom_Prefix))
	####_______________________________________
	cmds.rowColumnLayout(nc=3, columnOffset= ([1,"both",3],[2,"both",3],[3,"both",3]), p=clm)
	cmds.text(l='Add Custom Suffix...')
	Custom_Suffix = cmds.textField(w=150, text='_custom')
	cmds.button(l='Add',w=100, c=lambda x:Add_Custom_Suffix(Custom_Suffix))
	#####_______________________________________
	cmds.separator(h=2, st='none')
	cmds.rowColumnLayout( nc=3, co=([1,"both",5],[2,"both",5],[3,"both",5]),p=clm)
	rename_F = cmds.textField( text='name' )
	padding_F = cmds.intField( v=1 )
	cmds.button(l='Rename and Number', w=170, 
	                  c=lambda x:rename_and_number(rename_F,padding_F))
	cmds.setParent('..')
	cmds.separator(st='in', h=10)
    
    #####________________search and replace___________________________
	cmds.rowColumnLayout( nc=3, co=([1,"both",10],[2,"both",10]),p=clm)
	cmds.text(l='Search...')
	search_text = cmds.textField(w=150)
	All_Attr = cmds.checkBox(l='All Attributes')
	cmds.separator(h=2, st='none')
	cmds.separator(h=2, st='none')
	cmds.separator(h=2, st='none')
	cmds.text(l='Replace...')
	replace_text = cmds.textField(w=150)
	cmds.button(l='Lock | Hide', c=lambda x:Lock_and_Hide_Attr(All_Attr))
	cmds.separator(h=5, st='none')
	cmds.separator(h=5, st='none')
	cmds.separator(h=5, st='none')
	cmds.separator(w=10, st='none')
	cmds.button(l='search and replace', h=30, w=200, c=lambda x:search_and_replace(search_text,replace_text))
	cmds.button(l='Show', c=lambda x:Show_Attr(All_Attr))
    
    # --------------------- HELP TAB ---------------------------
	cmds.columnLayout(adj=1, p=helper_tab)
	cmds.separator(h=10, st='none')
	# help text
	helptext = "Auto Ctrl Maker \nVersion: 2.10 \nby Aashi Shukla\n-------------------------------------------------------\n\nThe Auto Ctrl Maker allows you to create a fully functional rig based on the deformable objects provided to it. If the joints are provided, it will make the ctrls from the radius, shape and colors specified by the user. If the shapes are provided, two new options of choosing joint placement and adding skinCluster also open up. \n\nSome more options such as Match Orient, Joint Chain, Shape Change and various Renaming Tools are available in the UTILITY Tab.\n\n Key Points: \n 1.The color slider works for individual ctrls from other rigs as well as in union with the Create and Build function on both ends. \n\n 2.Speaking of which, if you don't want the Global Ctrl or Rig Groups, just click on the 'Create' button but if you want them, click on the 'Build' function. Some of the functions that do not work together are already disabled. \n\n 3.The joint chain will be formed in the exact order in which the joints are selected, so kindly be mindful of that. \n\n 4.All the functions in the UTILITY tab can be used in any rig. \n\n\n SHAPE CHANGE TOOL \n\n How to use: \n\n (a) Load all the Ctrls whose shape you want to change. \n\n (b) Select the new shape of the Ctrls. \n\n (c) Click on the 'Shape Change Button'.\n\n-------------------------------------------------------\n(Maya 2023 and all previous versions supported)\n\n\nReport any bugs at: aashi41207@gmail.com \nThank You! I hope that this tool proves to be useful asset in your rigging mania."
	cmds.scrollField ( text = helptext, w = 410, h = 410, editable = False, wordWrap = True )
	
	# Display the window
	cmds.showWindow(Win)
	
if __name__ == "__main__":
	GUI()













# =========================================================================================
# ======================ATTRIBUTE LOCK FUNCTIONS===========================================
# =========================================================================================
def Joint_Provided_Switch(FK_Chain, Make_Ctrl_Button, Joint_Pos_Text, Add_Skin_Cluster_Text, ps_01,ps_02,sk_01,sk_02, state, *args):
	if state:
		cmds.button(Make_Ctrl_Button, e=1, enable=True)
		cmds.checkBox(FK_Chain, e=1, enable=True)
		cmds.text( Joint_Pos_Text, e=1, enable=False)
		cmds.text( Add_Skin_Cluster_Text, e=1, enable=False)
		cmds.radioButton(ps_01, e=1, enable=False)
		cmds.radioButton(ps_02, e=1, enable=False)
		cmds.radioButton(sk_01, e=1, enable=False)
		cmds.radioButton(sk_02, e=1, enable=False)
	else:
		cmds.button(Make_Ctrl_Button, e=1, enable=False)
		cmds.checkBox(FK_Chain, e=1, enable=False)
		cmds.text( Joint_Pos_Text, e=1, enable=True)
		cmds.text( Add_Skin_Cluster_Text, e=1, enable=True)
		cmds.radioButton(ps_01, e=1, enable=True)
		cmds.radioButton(ps_02, e=1, enable=True)
		cmds.radioButton(sk_01, e=1, enable=True)
		cmds.radioButton(sk_02, e=1, enable=True)			

def Make_Rig_Group(Add_Global_Text, Rig_Name_Text, Rig_Name, gb_01, gb_02, state,*args):
	if state:
		cmds.text( Add_Global_Text, e=1, enable=True)
		cmds.text(Rig_Name_Text, e=1, enable=True)
		cmds.textField(Rig_Name, e=1, enable=True)
		cmds.radioButton( gb_01, e=1, enable=True)
		cmds.radioButton( gb_02, e=1, enable=True)
		
	else:
		cmds.text( Add_Global_Text, e=1, enable=False)
		cmds.text(Rig_Name_Text, e=1, enable=False)
		cmds.textField(Rig_Name, e=1, enable=False)
		cmds.radioButton( gb_01, e=1, enable=False)
		cmds.radioButton( gb_02, e=1, enable=False)

		
def  Lock_Global_Attr_Switch(Global_Attr_Text,Attr_01,Attr_02,Attr_03,Attr_04,Attr_05, state, *args):
	if state:
		cmds.text( Global_Attr_Text, e=1, enable=False)
		cmds.checkBox(Attr_01, e=1, enable=False)
		cmds.checkBox(Attr_02, e=1, enable=False)
		cmds.checkBox(Attr_03, e=1, enable=False)
		cmds.checkBox(Attr_04, e=1, enable=False)
		cmds.checkBox(Attr_05, e=1, enable=False)
	else:
		cmds.text( Global_Attr_Text, e=1, enable=True)
		cmds.checkBox(Attr_01, e=1, enable=True)
		cmds.checkBox(Attr_02, e=1, enable=True)
		cmds.checkBox(Attr_03, e=1, enable=True)
		cmds.checkBox(Attr_04, e=1, enable=True)
		cmds.checkBox(Attr_05, e=1, enable=True)
# --------------------------------------------------------------------------------------------------
# ============================= RENAME TOOLS ===========================================
def Rename_Tool(Prefix, Padding, Suffix):
	prefix = cmds.textField( Prefix, text=True, query=True)
	padding = cmds.intField( Padding, value=True, query=True)
	suffix = cmds.textField( Suffix, text=True, query=True)
	
	print('New name: ', prefix, '_', padding, '_', suffix)
	name_list= cmds.ls(sl=True)
	
	for count,obj in enumerate(name_list):
		
		cmds.rename( obj, prefix + '_' + str(count+1).zfill(padding) + '_' + suffix )
# ---------------------------------------------------------------------------------------------------
def Remove_FC(*args):
	remove_FC_list = cmds.ls(sl=True)
	
	for item in remove_FC_list:
		cmds.rename( item, item[1:])
# -------------------------------------
def Remove_LC(*args):
	remove_LC_list = cmds.ls(sl=True)
	
	for item in remove_LC_list:
		cmds.rename( item, item[:-1])
# --------------------------------------
def suf_Jnt(*args):
	list = cmds.ls(sl=True)
	for item in list:
		cmds.rename( item, item + '_Jnt')
# ---------------------------------------
def suf_Geo(*args):
	list = cmds.ls(sl=True)
	for item in list:
		cmds.rename( item, item + '_Geo')
# ---------------------------------------
def suf_Grp(*args):
	list = cmds.ls(sl=True)
	for item in list:
		cmds.rename( item, item + '_Grp')
# ---------------------------------------
def suf_Ctrl(*args):
	list = cmds.ls(sl=True)
	for item in list:
		cmds.rename( item, item + '_Ctrl')
# ---------------------------------------
def suf_CON(*args):
	list = cmds.ls(sl=True)
	for item in list:
		cmds.rename( item, item + '_CON')
# ---------------------------------------
def suf_OFF(*args):
	list = cmds.ls(sl=True)
	for item in list:
		cmds.rename( item, item + '_OFF')
# ---------------------------------------
def Add_Custom_Prefix(Custom_Prefix):
	custom_prefix = cmds.textField(Custom_Prefix, query=True, text=True)
	
	custom_list = cmds.ls(sl=True)
	for item in custom_list:
		cmds.rename(item, custom_prefix + item)
# ----------------------------------------- 
def Add_Custom_Suffix(Custom_Suffix):
	custom_suffix = cmds.textField(Custom_Suffix, query=True, text=True)
	
	custom_list = cmds.ls(sl=True)
	for item in custom_list:
		cmds.rename(item, item + custom_suffix)
# ----------------------------------------------
def rename_and_number(rename_F,padding_F):
	name= cmds.textField(rename_F, text=True, query=True)
	number= cmds.intField(padding_F, value=True, query=True)
	print('name: ', name, 'padding: ', number)
	rn_list= cmds.ls(sl=True)
	for count, item in enumerate(rn_list):
		cmds.rename( item , name + str(count+1).zfill(number) )
# -------------------------------------------------------------------------
def search_and_replace(search_text,replace_text):
	Search_TEXT = cmds.textField(search_text, query=True, text=True)
	Replace_TEXT = cmds.textField(replace_text, query=True, text=True)
	
	replace_list = cmds.ls(sl=True)
	
	for name in replace_list:
		New_Name= name.replace(Search_TEXT,Replace_TEXT)
		cmds.rename( name, New_Name) 
	
# ====================================================================================
# ============CONTROLLERS COLOR FUNCTION SEPERATE=====================================
# ====================================================================================	
def Ctrl_Color_Tool(Color):
	col = cmds.colorIndexSliderGrp( Color, query=True, value=True)
	color_list = cmds.ls(sl=True)
	print('Color: ', col)
	for item in color_list:
		shape_node = cmds.listRelatives(item , s=True)[0]
		cmds.setAttr( shape_node + '.overrideEnabled', 1 )
		cmds.setAttr( shape_node + '.overrideColor', col-1 )
		
# ------------------------------------------------------------------------------
def Make_C(Radius, Color, FK_Chain, PC, SC):
	current_shape= cmds.optionMenuGrp('Ctrl_Sel_Menu', query=True, value=True)
	n = cmds.floatField( Radius, query=True, value=True)
	col = cmds.colorIndexSliderGrp( Color, query=True, value=True)
	pc = cmds.checkBox( PC, query=True, value=True)
	sc = cmds.checkBox( SC, query=True, value=True)
	make_fk = cmds.checkBox( FK_Chain, query=True, value=True)
	# Check if the selection is valid or not
	sel_check = cmds.ls(sl=True, type='joint')
	All_Ctrl_List = []
	# Error to make sure joint is selected:
	if not sel_check:
		cmds.error("Please provide joints", n=True)
	else:
		joint_list = cmds.ls(sl=True)
		print('Joint is provided')
		for item in joint_list:
			# ======================================================
			# Make Controllers for every joint
			cmds.select(cl=True)
			print('Radius: ', n)
			if current_shape == 'cube':
				item01 = cmds.curve(n= item + '_C', d=1, p=[(-n, n, n), (-n, -n, n),(n, -n, n),(n, n, n),(-n, n, n), 
				(-n, n, -n), (-n, -n, -n), (n, -n, -n), (n, n, -n), (-n, n, -n), (n, n, -n), (n, n, n), 
				(n, -n, n), (n, -n, -n), (-n, -n, -n), (-n, -n, n)]) 
				
			elif current_shape == 'circle':
				item01 = cmds.circle( radius=n, n= item + '_C')
				cmds.xform(item + '_C', ro=(-90,0,0), r=True, os=True)
				cmds.makeIdentity(item + '_C', apply=True, t=1, r=1, s=1)
				
			elif current_shape == 'square':
				item01 = cmds.curve(n= item + '_C', d=1, p=[(-n, 0, -n),(n,0,-n),(n,0,n),(-n,0,n),(-n,0,-n)])
				
			elif current_shape == 'triangle':
				item01 = cmds.curve(n= item + '_C', d=1, p=[(n,0,n),(-n,0,0),(n,0,-n),(n,0,n)] )
				
			elif current_shape == 'Hexagon':
				item01 = cmds.circle( name= item + '_C', radius=n, d=1, s=6)
				cmds.xform(item + '_C', ro=(90,0,0))
				cmds.makeIdentity(item + '_C', apply=True, t=1, s=1, r=1)
				
			elif current_shape == 'COG':
				m = n*0.5
				item01 = cmds.circle( radius=n, n= item + '_C')
				cmds.xform(item + '_C', ro=(90,0,0), r=True, os=True)
				cmds.makeIdentity( item + '_C', apply=True, t=1, r=1, s=1)
				cmds.curve( n='COG_C2', d=1, p=[(-1.25*m, 0, -1.25*m),(-1.25*m, 0, -3.75*m), (-2.5*m, 0, -3.75*m),
				(0,0,-6.25*m),(2.5*m,0,-3.75*m),(1.25*m, 0, -3.75*m),(1.25*m, 0 ,-1.25*m),(3.75*m, 0, -1.25*m),(3.75*m,0,-2.5*m), 
				(6.25*m ,0 ,0 ),(3.75*m, 0, 2.5*m),(3.75*m ,0 ,1.25*m), (1.25*m ,0, 1.25*m), (1.25*m ,0 ,3.75*m),(2.5*m, 0 ,3.75*m),
				(0 ,0, 6.25*m),(-2.5*m ,0, 3.75*m),(-1.25*m, 0 ,3.75*m),(-1.25*m, 0, 1.25*m),(-3.75*m, 0, 1.25*m),(-3.75*m ,0, 2.5*m ),
				(-6.25*m ,0 ,0 ), (-3.75*m, 0, -2.5*m),(-3.75*m ,0 ,-1.25*m ),( -1.25*m, 0, -1.25*m)])
				cmds.select( 'COG_C2.cv[0]','COG_C2.cv[6]','COG_C2.cv[12]','COG_C2.cv[18]','COG_C2.cv[24]' )
				cmds.scale( 1.57, 1.57, 1.57, r=True, ocp=True, xc='edge',a=True) 
				cmds.select(cl=True)
				rel = cmds.listRelatives( 'COG_C2', s=True)[0]
				
				cmds.setAttr( rel + '.overrideEnabled', 1 )
				cmds.setAttr( rel + '.overrideColor', col-1 )
				cmds.select( rel , item + '_C')
				cmds.parent (relative=True, s=True)
				cmds.delete('COG_C2')
				cmds.select(cl=True)
				
				
			elif current_shape == 'Plus':
				item01 = cmds.curve(n= item + '_C', d=1, p=[(n, 0 ,n ),( n, 0, 3*n),(-n, 0, 3*n),
				  (-n, 0, n),(-3*n, 0, n), (-3*n, 0, -n), (-n, 0, -n), (-n, 0, -3*n),
				  ( n, 0, -3*n),(n, 0, -n), (3*n, 0, -n), (3*n,0, n), (n, 0, n)] ) 
				
			elif current_shape == 'Arrow':
				m = n*0.5
				item01 = cmds.curve(n= item + '_C', d=1, p=[(-1.25*m, 0, 2.5*m), (-1.25*m,0,0), (-2.5*m,0,0),
				(0,0,-2.5*m),(2.5*m,0,0),(1.25*m,0,0),(1.25*m,0,2.5*m), (-1.25*m, 0,2.5*m)] )
				
			elif current_shape == 'locator':
				item01 = cmds.curve(n= item + '_C' ,d=1,p=[(0, 1.25*n, 0), (0, 0, 0), (0,-1.25*n, 0),(0,0,0),
				(1.25*n,0,0) ,(0,0,0),(-1.25*n,0,0),(0,0,0),(0,0,1.25*n),(0,0,0),(0,0,-1.25*n)] )  
				
			else:
				cmds.error('Invalid option!')
			
			# ===================================================================================
			# Offset groups for controls
			item02 = cmds.group( item + '_C', n = item + '_C_Grp' )
			item03 = cmds.group( item + '_C_Grp', n = item + '_C_Grp1' )
			
			All_Ctrl_List.append(item03)
			All_Ctrl_List.append(item02)
			All_Ctrl_List.append(item01)
			# ===================================================================================
			# Positioning the controller groups(pos of Ctrls at their joints that are provided)
			cmds.delete(cmds.parentConstraint( item , item + '_C_Grp1' ))
			# ====================================================================================
			# Constraints:
			if pc==1:
					cmds.parentConstraint(item + '_C', item  , mo=True)
			
			if sc==1:
				cmds.scaleConstraint(item + '_C', item , mo=True )
				
			# ====================================================================================
			# Color of controls:
			print('Color: ', col)
			shape_node = cmds.listRelatives(item + '_C' , s=True)[0]
			cmds.setAttr( shape_node + '.overrideEnabled', 1 )
			cmds.setAttr( shape_node + '.overrideColor', col-1 )
			cmds.select(cl=True)
		if make_fk == 1:
			
			i=3
			for item in enumerate(All_Ctrl_List):
				if i!= len(All_Ctrl_List):
					cmds.parent( All_Ctrl_List[i],All_Ctrl_List[i-1] )
					i+=3
			

# ==================================================================================================
# ==================================== OTHERS TAB ==================================================
# ==================================================================================================
def Make_Parent_Chain(*args):
	chain= cmds.ls(sl=True)
	i=1
	for jnt in chain:
		cmds.parent( chain[i], chain[i-1])
		i+=1
	print('parent chain made')

# =================================================================================================
def Parent_Chain_Exp(*args):
	# create new explaination window
	P_win=cmds.window('Joint_Chain_Explain', t='Joint Chain',wh=(200,200), mxb=0, mnb=0, sizeable=1)
	tab_lay= cmds.tabLayout(imh=5, imw=5)
	help_tab = cmds.formLayout(p=tab_lay)
	cmds.formLayout(help_tab, edit=True)
	cmds.columnLayout(adj=1)
	cmds.tabLayout(tab_lay, edit=True, tabLabel=(help_tab, "Help"))
	cmds.text( al='left', l='Joint chain command:')
	cmds.text( al='left', l='1. Select the joints in order you want them to be parented.')
	cmds.text( al='left', l='2. Click on the Joint Chain Button.')
	cmds.text( al='left', l='A chain will be created based on the order of joints\nthat you have provided.')
	cmds.separator(st='in')
	cmds.showWindow(P_win)
# ============================================================================
def Match_Orient(*args):
	list= cmds.ls(sl=True)
	if len(list)<1:
		cmds.error("Select 2 objects: a parent and a child", n=True)
	else:
		parent_T= list[0]
		child_T= list[1]
		cmds.delete(cmds.parentConstraint(parent_T, child_T, mo=False))
		print('matched')
# ===========================================================================
def Match_Orient_Exp(*args):
	# create new explaination window
	P_win=cmds.window('Match_Orient_Explain', t='Match Orient',wh=(200,200), mxb=0, mnb=0, sizeable=1)
	tab_lay= cmds.tabLayout(imh=5, imw=5)
	help_tab = cmds.formLayout(p=tab_lay)
	cmds.formLayout(help_tab, edit=True)
	cmds.columnLayout(adj=1)
	cmds.tabLayout(tab_lay, edit=True, tabLabel=(help_tab, "Help"))
	cmds.text( al='left', l='Match Orient command:')
	cmds.text( al='left', l='1. Select the parent object.')
	cmds.text( al='left', l='2. Shift Select the child object.')
	cmds.text( al='left', l='3. Click Button.')
	cmds.separator(st='in')
	cmds.showWindow(P_win)
# ================================================================================
def Joint_Place_Center(*args):
	shape_list = cmds.ls(sl=True)
	
	if len(shape_list)<1:
		cmds.error("Select something!", n=True)
	else:
		for shape in shape_list:
			cmds.select(cl=True)
			cmds.joint( n = shape + '_Jnt')
			cmds.delete(cmds.parentConstraint(cmds.cluster(shape, n='cls'), shape + '_Jnt'))
			cmds.delete('cls')
			
# =================================================================================
def Joint_Place_Pivot(*args):
	shape_list = cmds.ls(sl=True)
	if len(shape_list)<1:
		cmds.error("Select something!", n=True)
	else:
		for shape in shape_list:
			cmds.select(cl=True)
			cmds.joint( n = shape + '_Jnt' )
			cmds.delete(cmds.parentConstraint( shape, shape + '_Jnt' ))

# ================================================================================
def button_wrapper(fn, *args, **kwargs):
	def wrapped():
		fn(*args, **kwargs)
	return wrapped
	
def Load_Shape(shape_change):
	global selection_for_shape_change
	selection_for_shape_change = cmds.ls(sl=True)
	cmds.textField(shape_change, e=1, text= selection_for_shape_change[0])

def Change_Shape(Radius , Color , *args):
	global selection_for_shape_change
	i=0
	change_shape = cmds.optionMenuGrp('Ctrl_Change_Menu', query=True, value=True)
	col_value = cmds.colorIndexSliderGrp( Color, value=True, query=True)
	n = cmds.floatField(Radius, query=True, value=True)
	print('Radius: ', n)
	for item in selection_for_shape_change:
		# create change shapes
		if change_shape == 'cube':
			cmds.curve(n= item + '_C1', d=1, p=[(-n, n, n), (-n, -n, n),(n, -n, n),(n, n, n),(-n, n, n), 
			(-n, n, -n), (-n, -n, -n), (n, -n, -n), (n, n, -n), (-n, n, -n), (n, n, -n), (n, n, n), 
			(n, -n, n), (n, -n, -n), (-n, -n, -n), (-n, -n, n)]) 
					
		elif change_shape == 'circle':
			cmds.circle( radius=n, n= item + '_C1')
			cmds.xform(item + '_C1', ro=(-90,0,0), r=True, os=True)
			cmds.makeIdentity(item + '_C1', apply=True, t=1, r=1, s=1)
			
		elif change_shape == 'square':
			cmds.curve(n= item + '_C1', d=1, p=[(-n, 0, -n),(n,0,-n),(n,0,n),(-n,0,n),(-n,0,-n)])
			
		elif change_shape == 'triangle':
			cmds.curve(n= item + '_C1', d=1, p=[(n,0,n),(-n,0,0),(n,0,-n),(n,0,n)] )
			
		elif change_shape == 'Hexagon':
			cmds.circle( name= item + '_C1', radius=n, d=1, s=6)
			cmds.xform(item + '_C1', ro=(90,0,0))
			cmds.makeIdentity(item + '_C1', apply=True, t=1, s=1, r=1)
						
		elif change_shape == 'Plus':
			cmds.curve(n= item + '_C1', d=1, p=[(n, 0 ,n ),( n, 0, 3*n),(-n, 0, 3*n),
			  (-n, 0, n),(-3*n, 0, n), (-3*n, 0, -n), (-n, 0, -n), (-n, 0, -3*n),
			  ( n, 0, -3*n),(n, 0, -n), (3*n, 0, -n), (3*n,0, n), (n, 0, n)] ) 
			
		elif change_shape == 'Arrow':
			m = n*0.5
			cmds.curve(n= item + '_C1', d=1, p=[(-1.25*m, 0, 2.5*m), (-1.25*m,0,0), (-2.5*m,0,0),
			(0,0,-2.5*m),(2.5*m,0,0),(1.25*m,0,0),(1.25*m,0,2.5*m), (-1.25*m, 0,2.5*m)] )
			
		elif change_shape == 'locator':
			cmds.curve(n= item + '_C1' ,d=1, p=[(0, 1.25*n, 0), (0, 0, 0), (0,-1.25*n, 0),(0,0,0),
			(1.25*n,0,0) ,(0,0,0),(-1.25*n,0,0),(0,0,0),(0,0,1.25*n),(0,0,0),(0,0,-1.25*n)] )
			
		else:
			cmds.error('Invalid option!')
		shape_node= cmds.listRelatives(item + '_C1', s=1)[0]

		cmds.delete(cmds.listRelatives(selection_for_shape_change[i], s=True))
		cmds.parent(shape_node,selection_for_shape_change[i], r=True, shape=True)
		cmds.delete(item + '_C1')
		# color of the changed controls
		cmds.setAttr( shape_node + '.overrideEnabled',1)
		cmds.setAttr( shape_node + '.overrideColor',col_value - 1)
		i+=1
# ----------------------------------------------------------------------
def Lock_and_Hide_Attr(All_Attr):
	all_attr= cmds.checkBox(All_Attr, query=True, value=True)
	list = cmds.ls(sl=True)
	if all_attr == 1:
		for objs in list:
			cmds.setAttr( objs + '.translateX', k=False, cb=False, l=True)
			cmds.setAttr( objs + '.translateY', k=False, cb=False, l=True)
			cmds.setAttr( objs + '.translateZ', k=False, cb=False, l=True)
			cmds.setAttr( objs + '.rotateX', k=False, cb=False, l=True)
			cmds.setAttr( objs + '.rotateY', k=False, cb=False, l=True)
			cmds.setAttr( objs + '.rotateZ', k=False, cb=False, l=True)
			cmds.setAttr( objs + '.scaleX', k=False, cb=False, l=True)
			cmds.setAttr( objs + '.scaleY', k=False, cb=False, l=True)
			cmds.setAttr( objs + '.scaleZ', k=False, cb=False, l=True)
			cmds.setAttr( objs + '.visibility', k=False, cb=False, l=True)
# ------------------------------------------------------------------------
def Show_Attr(All_Attr):
	
	all_attr= cmds.checkBox(All_Attr, query=True, value=True)
	list = cmds.ls(sl=True)
	if all_attr == 1:
		for objs in list:
			cmds.setAttr( objs + '.translateX', cb=True, l=False)
			cmds.setAttr( objs + '.translateY', cb=True, l=False)
			cmds.setAttr( objs + '.translateZ', cb=True, l=False)
			cmds.setAttr( objs + '.rotateX', cb=True, l=False)
			cmds.setAttr( objs + '.rotateY', cb=True, l=False)
			cmds.setAttr( objs + '.rotateZ', cb=True, l=False)
			cmds.setAttr( objs + '.scaleX', cb=True, l=False)
			cmds.setAttr( objs + '.scaleY', cb=True, l=False)
			cmds.setAttr( objs + '.scaleZ', cb=True, l=False)
			cmds.setAttr( objs + '.visibility', cb=True, l=False)
			# make them keyable
			cmds.setAttr( objs + '.translateX', k=True)
			cmds.setAttr( objs + '.translateY', k=True)
			cmds.setAttr( objs + '.translateZ',k=True)
			cmds.setAttr( objs + '.rotateX', k=True)
			cmds.setAttr( objs + '.rotateY', k=True)
			cmds.setAttr( objs + '.rotateZ', k=True)
			cmds.setAttr( objs + '.scaleX', k=True)
			cmds.setAttr( objs + '.scaleY',k=True)
			cmds.setAttr( objs + '.scaleZ', k=True)
			cmds.setAttr( objs + '.visibility', k=True)




# ==================================================================================================
# ++++++++++++++++++++++++++++++++++++ MAIN ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ==================================================================================================
def Create(Radius,Color,Jnt_Prvd,FK_Chain, ps_01,ps_02,sk_01,PC,SC,Make_Grp,Rig_Name,gb_01, Attr_01,Attr_02,Attr_03,Attr_04,Attr_05):
	pc = cmds.checkBox( PC, query=True, value=True)
	sc = cmds.checkBox( SC, query=True, value=True)
	
	attr_01 = cmds.checkBox( Attr_01 , query=True, value=True)
	attr_02 = cmds.checkBox( Attr_02 , query=True, value=True)
	attr_03 = cmds.checkBox( Attr_03 , query=True, value=True)
	attr_04 = cmds.checkBox( Attr_04 , query=True, value=True)
	attr_05 = cmds.checkBox( Attr_05 , query=True, value=True)
	make_grp = cmds.checkBox( Make_Grp, query=True, value=True)
	
	n = cmds.floatField( Radius, query=True, value=True)
	
	col = cmds.colorIndexSliderGrp( Color, query=True, value=True)
	
	current_shape= cmds.optionMenuGrp('Ctrl_Sel_Menu', query=True, value=True)
	
	make_fk = cmds.checkBox(FK_Chain, query=True, value=True)
	
	rig_name = cmds.textField(Rig_Name, query=True, text=True)
	ALL_CTRL_LIST = []
	if cmds.checkBox(Jnt_Prvd, query=True, value=True):
		# Check if the selection is valid or not
		sel_check = cmds.ls(sl=True, type='joint')
		# Error to make sure joint is selected:
		if not sel_check:
			cmds.error("Please provide joints...", n=0)
		else:
			joint_list = cmds.ls(sl=True)
			print('Joint is provided')
			for item in joint_list:
				
				# ============================================================================================
				# Make Controllers for every joint
				cmds.select(cl=True)
				print('Radius: ', n)
				if current_shape == 'cube':
					Ctrl_01 = cmds.curve(n= item + '_C', d=1, p=[(-n, n, n), (-n, -n, n),(n, -n, n),(n, n, n),(-n, n, n), 
					(-n, n, -n), (-n, -n, -n), (n, -n, -n), (n, n, -n), (-n, n, -n), (n, n, -n), (n, n, n), 
					(n, -n, n), (n, -n, -n), (-n, -n, -n), (-n, -n, n)]) 
					
				elif current_shape == 'circle':
					Ctrl_01 = cmds.circle( radius=n, n= item + '_C')
					cmds.xform(item + '_C', ro=(-90,0,0), r=True, os=True)
					cmds.makeIdentity(item + '_C', apply=True, t=1, r=1, s=1)
					
				elif current_shape == 'square':
					Ctrl_01 = cmds.curve(n= item + '_C', d=1, p=[(-n, 0, -n),(n,0,-n),(n,0,n),(-n,0,n),(-n,0,-n)])
					
				elif current_shape == 'triangle':
					Ctrl_01 = cmds.curve(n= item + '_C', d=1, p=[(n,0,n),(-n,0,0),(n,0,-n),(n,0,n)] )
					
				elif current_shape == 'Hexagon':
					Ctrl_01 = cmds.circle( name= item + '_C', radius=n, d=1, s=6)
					cmds.xform(item + '_C', ro=(90,0,0))
					cmds.makeIdentity(item + '_C', apply=True, t=1, s=1, r=1)
					
				elif current_shape == 'COG':
					m = n*0.5
					Ctrl_01 = cmds.circle( radius=n, n= item + '_C')
					cmds.xform(item + '_C', ro=(90,0,0), r=True, os=True)
					cmds.makeIdentity( item + '_C', apply=True, t=1, r=1, s=1)
					cmds.curve( n='COG_C2', d=1, p=[(-1.25*m, 0, -1.25*m),(-1.25*m, 0, -3.75*m), (-2.5*m, 0, -3.75*m),
					(0,0,-6.25*m),(2.5*m,0,-3.75*m),(1.25*m, 0, -3.75*m),(1.25*m, 0 ,-1.25*m),(3.75*m, 0, -1.25*m),(3.75*m,0,-2.5*m), 
					(6.25*m ,0 ,0 ),(3.75*m, 0, 2.5*m),(3.75*m ,0 ,1.25*m), (1.25*m ,0, 1.25*m), (1.25*m ,0 ,3.75*m),(2.5*m, 0 ,3.75*m),
					(0 ,0, 6.25*m),(-2.5*m ,0, 3.75*m),(-1.25*m, 0 ,3.75*m),(-1.25*m, 0, 1.25*m),(-3.75*m, 0, 1.25*m),(-3.75*m ,0, 2.5*m ),
					(-6.25*m ,0 ,0 ), (-3.75*m, 0, -2.5*m),(-3.75*m ,0 ,-1.25*m ),( -1.25*m, 0, -1.25*m)])
					cmds.select( 'COG_C2.cv[0]','COG_C2.cv[6]','COG_C2.cv[12]','COG_C2.cv[18]','COG_C2.cv[24]' )
					cmds.scale( 1.57, 1.57, 1.57, r=True, ocp=True, xc='edge',a=True) 
					cmds.select(cl=True)
					rel = cmds.listRelatives( 'COG_C2', s=True)[0]
					
					cmds.setAttr( rel + '.overrideEnabled', 1 )
					cmds.setAttr( rel + '.overrideColor', col-1 )
					cmds.select( rel , item + '_C')
					cmds.parent (relative=True, s=True)
					cmds.delete('COG_C2')
					cmds.select(cl=True)
					
				elif current_shape == 'Plus':
					Ctrl_01 = cmds.curve(n= item + '_C', d=1, p=[(n, 0 ,n ),( n, 0, 3*n),(-n, 0, 3*n),
					  (-n, 0, n),(-3*n, 0, n), (-3*n, 0, -n), (-n, 0, -n), (-n, 0, -3*n),
					  ( n, 0, -3*n),(n, 0, -n), (3*n, 0, -n), (3*n,0, n), (n, 0, n)] ) 
					
				elif current_shape == 'Arrow':
					m = n*0.5
					Ctrl_01 = cmds.curve(n= item + '_C', d=1, p=[(-1.25*m, 0, 2.5*m), (-1.25*m,0,0), (-2.5*m,0,0),
					(0,0,-2.5*m),(2.5*m,0,0),(1.25*m,0,0),(1.25*m,0,2.5*m), (-1.25*m, 0,2.5*m)] )
					
				elif current_shape == 'locator':
					Ctrl_01 = cmds.curve(n= item + '_C' ,d=1,p=[(0, 1.25*n, 0), (0, 0, 0), (0,-1.25*n, 0),(0,0,0),
					(1.25*n,0,0) ,(0,0,0),(-1.25*n,0,0),(0,0,0),(0,0,1.25*n),(0,0,0),(0,0,-1.25*n)] )
					
				else:
					cmds.error('Invalid option!')
				# The individual Ctrl is created: Now we make OFFSET grps for each
				Ctrl_02 = cmds.group( item + '_C', n = item + '_C_Grp' )
				Ctrl_03 = cmds.group( item + '_C_Grp', n = item + '_C_Grp1' )
				ALL_CTRL_LIST.append(Ctrl_03)
				ALL_CTRL_LIST.append(Ctrl_02)
				ALL_CTRL_LIST.append(Ctrl_01)
				# Positioning the controller groups(pos of Ctrls at their joints that are provided)
				cmds.delete(cmds.parentConstraint( item , item + '_C_Grp1' ))
				# ===========================================================================================
				# Constrain the Joints with their Ctrls:
				if pc==1:
					cmds.parentConstraint(item + '_C', item  , mo=True)
					
				if sc==1:
					cmds.scaleConstraint(item + '_C', item , mo=True )
					
				# ===========================================================================================
				# Color of controls (Assigning the colors to the controls)
				print('Color: ', col)
				shape_node = cmds.listRelatives(item + '_C' , s=True)[0]
				cmds.setAttr( shape_node + '.overrideEnabled', 1 )
				cmds.setAttr( shape_node + '.overrideColor', col-1 )
				cmds.select(cl=True)
				
			# make fk chain:
			if make_fk == 1:
				i=3
				for item in enumerate(ALL_CTRL_LIST):
					if i!= len(ALL_CTRL_LIST):
						cmds.parent(ALL_CTRL_LIST[i],ALL_CTRL_LIST[i-1] )
						i+=3
				print('FK CHAIN MADE_')
				cmds.select(cl=True)
				# If the make grp option is selected make groups
				if make_grp==1:
					cmds.group(em=1, n = "Ctrl_Grp" )
					cmds.parent( ALL_CTRL_LIST[0] , "Ctrl_Grp" )
					
					cmds.group(joint_list, n="Joint_Grp")
					
					cmds.group(em=True, n="Mesh_Grp")
					
					cmds.group("Mesh_Grp","Joint_Grp","Ctrl_Grp", n="RIG")
					
					# Renaming in Overall Grps
					cmds.select(cl=True)
					cmds.select("RIG", hierarchy = True)
					Renaming_Rig_List = cmds.ls(sl=True)
					
					for count, item in enumerate(Renaming_Rig_List):
						cmds.rename( item, str(rig_name) + '_' + item)
				else:
					print("Group not made, option was not selected")
					
				
				# If Global Ctrl option is on, make Global Ctrl with FK
				if cmds.radioButton(gb_01, query=True, select=True):
					Global_Rename_List = []
					# Main_C
					x = n*3
					cmds.curve(n= 'Main_C', d=1, p=[(-x, 0, -x),(x,0,-x),(x,0,x),(-x,0,x),(-x,0,-x)])
					cmds.group('Main_C', n= 'Main_C_Offset')
					
					# add Main in rename list----
					Global_Rename_List.append('Main_C')
					Global_Rename_List.append('Main_C_Offset')
					
					cmds.select(cl=True)
					# Color of Main_C
					Glb = cmds.listRelatives('Main_C' , s=True)[0]
					cmds.setAttr(Glb + '.overrideEnabled', 1 )
					cmds.setAttr(Glb + '.overrideColor', 13 )
					# Making Global_C
					cmds.circle( r=n*5 , d=1, s=6, n= 'Global_C')
					cmds.xform('Global_C', ro=(90,0,0))
					cmds.makeIdentity('Global_C', apply=True, t=1, s=1, r=1)
					cmds.group('Global_C', n= 'Global_C_Offset')
					
					# add Global in rename list-------
					Global_Rename_List.append('Global_C')
					Global_Rename_List.append('Global_C_Offset')
					
					cmds.select(cl=True)
					# Color of Global_C
					Plc = cmds.listRelatives('Global_C' , s=True)[0]
					cmds.setAttr(Plc + '.overrideEnabled', 1 )
					cmds.setAttr(Plc + '.overrideColor', 14 )
					# Connect Main and Global Ctrls
					cmds.parent('Main_C_Offset','Global_C')
					# Parent All existing ctrl groups under the Main_C
					cmds.parent(str(rig_name) + '_' + "Ctrl_Grp", 'Main_C')
					# Making the placement control: This will have scaling locked
					v=n*2.2
					cmds.curve( n='Placement_C', d=1, p=[(-1.25*v, 0, -1.25*v),(-1.25*v, 0, -3.75*v), (-2.5*v, 0, -3.75*v),(0,0,-6.25*v),
						(2.5*v,0,-3.75*v),(1.25*v, 0, -3.75*v),(1.25*v, 0 ,-1.25*v),(3.75*v, 0, -1.25*v),(3.75*v,0,-2.5*v), (6.25*v ,0 ,0 ),
						(3.75*v, 0, 2.5*v),(3.75*v ,0 ,1.25*v), (1.25*v ,0, 1.25*v), (1.25*v ,0 ,3.75*v),(2.5*v, 0 ,3.75*v),(0 ,0, 6.25*v),
						(-2.5*v ,0, 3.75*v),(-1.25*v, 0 ,3.75*v),(-1.25*v, 0, 1.25*v),(-3.75*v, 0, 1.25*v),(-3.75*v ,0, 2.5*v ),
						(-6.25*v ,0 ,0 ),(-3.75*v, 0, -2.5*v),(-3.75*v ,0 ,-1.25*v ),( -1.25*v, 0, -1.25*v)])
					cmds.select( 'Placement_C.cv[0]','Placement_C.cv[6]','Placement_C.cv[12]','Placement_C.cv[18]','Placement_C.cv[24]' )
					cmds.scale( 1.57, 1.57, 1.57, r=True, ocp=True, xc='edge',a=True)
					cmds.select( 'Placement_C.cv[1:5]', 'Placement_C.cv[7:11]', 'Placement_C.cv[13:17]', 'Placement_C.cv[19:23]')
					cmds.scale( 0.6, 0.6, 0.6, r=True, ocp=True)  
					cmds.select(cl=True)
					rell = cmds.listRelatives( 'Placement_C', s=True)[0]

					cmds.setAttr( rell + '.overrideEnabled', 1 )
					cmds.setAttr( rell + '.overrideColor', 16 )

					cmds.select(cl=True)
					# Grouping the Placement_C and placing it above all ctrls
					cmds.group('Placement_C', n='Placement_C_Offset')
					cmds.group('Placement_C_Offset', n = "CTRL_SYSTEM" )
					
					cmds.parent('Global_C_Offset', 'Placement_C')
					cmds.parent("CTRL_SYSTEM" , str(rig_name) + '_' + 'RIG')
					
					# adding Placement in rename list --------
					Global_Rename_List.append('Placement_C')
					Global_Rename_List.append('Placement_C_Offset')
					Global_Rename_List.append("CTRL_SYSTEM")
					
					# Locking the scale of Placement_C
					cmds.setAttr( 'Placement_C.scaleX', lock=True, channelBox=False, k=False)
					cmds.setAttr( 'Placement_C.scaleY', lock=True, channelBox=False, k=False)
					cmds.setAttr( 'Placement_C.scaleZ', lock=True, channelBox=False, k=False)
					cmds.setAttr( 'Placement_C.visibility', lock=True, channelBox=False, k=False)
					
					cmds.setAttr('Global_C.visibility', lock=True, channelBox=False, k=False)
					# Adding Global_C Attributes
					if attr_01:
						cmds.addAttr('Global_C', longName= 'Global_Scale', at='float', dv=1.00, max=10.0, min=0.1, keyable=True)
						cmds.setAttr('Global_C.Global_Scale', cb=True, keyable=False)  
						print('Global Scale added')
						
					if attr_02:
						cmds.addAttr('Global_C', longName= 'Mesh_Display', at='enum', en= "normal:template:reference", keyable=True)
						cmds.setAttr('Global_C.Mesh_Display', cb=True, keyable=False)
						print('Mesh Display added')
					
					if attr_03:
						cmds.addAttr('Global_C', longName= 'Mesh_VIS', min=0, max=1, dv=1, keyable=True)
						cmds.setAttr('Global_C.Mesh_VIS', cb=True, keyable=False)
						print('Mesh VIS added')
						
					if attr_04:
						cmds.addAttr('Global_C', longName= 'Ctrl_VIS', min=0, max=1, dv=1, keyable=True)
						cmds.setAttr('Global_C.Ctrl_VIS', cb=True, keyable=False)
						print('Ctrl VIS added')
						
					if attr_05:
						cmds.addAttr('Global_C', longName= 'Jnt_VIS', min=0, max=1, dv=0, keyable=True)
						cmds.setAttr('Global_C.Jnt_VIS', cb=True, keyable=False)
						print('Jnt VIS added')
						
					# Connecting all Global Scale Attributes
					cmds.connectAttr('Global_C.Global_Scale', 'Global_C.scaleX' )
					cmds.connectAttr('Global_C.Global_Scale', 'Global_C.scaleY' )
					cmds.connectAttr('Global_C.Global_Scale', 'Global_C.scaleZ' )

					cmds.setAttr('Global_C.scaleX', k=False, cb=False, l=True)
					cmds.setAttr('Global_C.scaleY', k=False, cb=False, l=True)
					cmds.setAttr('Global_C.scaleZ', k=False, cb=False, l=True)

					# Connecting Mesh Display with Override Display type
					cmds.setAttr( str(rig_name) + '_' + 'Mesh_Grp.overrideEnabled', 1)
					cmds.connectAttr('Global_C.Mesh_Display', str(rig_name) + '_' + 'Mesh_Grp.overrideDisplayType')
					# Setting default value to Reference, i.e. 2
					cmds.setAttr('Global_C.Mesh_Display', 2 )
					# Connecting Mesh_VIS
					cmds.connectAttr('Global_C.Mesh_VIS', str(rig_name) + '_' + 'Mesh_Grp.v')
					cmds.setAttr(str(rig_name) + '_' + 'Mesh_Grp.v', k=False, cb=True, l=True)
					# Connecting Ctrl_VIS
					cmds.connectAttr('Global_C.Ctrl_VIS', str(rig_name) + '_' + 'Ctrl_Grp.v')
					cmds.setAttr(str(rig_name) + '_' + 'Ctrl_Grp.v', k=False, cb=True, l=True)
					# Connecting Jnt_VIS
					cmds.connectAttr('Global_C.Jnt_VIS', str(rig_name) + '_' + 'Joint_Grp.v')
					cmds.setAttr(str(rig_name) + '_' + 'Joint_Grp.v', k=False, cb=True, l=True)

					# Finalising the RIG Group
					cmds.setAttr(str(rig_name) + '_' + 'RIG.translateX', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.translateY', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.translateZ', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.rotateX', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.rotateY', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.rotateZ', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.scaleX', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.scaleY', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.scaleZ', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.visibility', k=False, cb=True)
					# Lock and Hide Vis control of the Main_C
					cmds.setAttr('Main_C.visibility', k=False, cb=False, lock=True)

					# Lock and Hide of Visibility channel of the individual controls
					for ctrl in (cmds.ls('*_C')):
						cmds.setAttr( ctrl + ".v", k=False, cb=False, l=True)

					cmds.select(cl=True)

					for count, item in enumerate(Global_Rename_List):
						
						cmds.rename( item, str(rig_name) + '_' + item)
					
				else:
					print('Global Ctrl Option not selected')
					
			else:		
				# make groups and Global if FK Chain is not selected
				if make_grp==1:
					# Make groups for Geo, Jnts and Ctrls
					Ctrl_Grp_List = cmds.ls('*_C_Grp1')
					cmds.group(Ctrl_Grp_List, n="Ctrl_Grp")
					cmds.group(joint_list, n="Joint_Grp")
					cmds.group(em=True, n="Mesh_Grp")
					cmds.group("Mesh_Grp","Joint_Grp","Ctrl_Grp", n="RIG")
					
					# Renaming in Overall Grps
					cmds.select(cl=True)
					cmds.select("RIG", hierarchy = True)
					Renaming_Rig_List = cmds.ls(sl=True)
					
					
					for count, item in enumerate(Renaming_Rig_List):
						if cmds.objExists(item):
							cmds.rename( item, str(rig_name) + '_' + item)
				else:
					print("Group option not selected")
				# ============================================================================================
				# ===================================================================================
				# Making a Global Ctrl
				if cmds.radioButton(gb_01, query=True, select=True):
					Global_Rename_List = []
					x = n*3
					cmds.curve(n= 'Main_C', d=1, p=[(-x, 0, -x),(x,0,-x),(x,0,x),(-x,0,x),(-x,0,-x)] )
					cmds.group('Main_C', n= 'Main_C_Offset')
					cmds.select(cl=True)
					# add in list------
					Global_Rename_List.append('Main_C')
					Global_Rename_List.append('Main_C_Offset')
					# Color of Main_C
					Glb = cmds.listRelatives('Main_C' , s=True)[0]
					cmds.setAttr(Glb + '.overrideEnabled', 1 )
					cmds.setAttr(Glb + '.overrideColor', 13 )
					# Making Global_C
					cmds.circle( r=n*5 , d=1, s=6, n= 'Global_C')
					cmds.xform('Global_C', ro=(90,0,0))
					cmds.makeIdentity('Global_C', apply=True, t=1, s=1, r=1)
					cmds.group('Global_C', n= 'Global_C_Offset')
					cmds.select(cl=True)
					# add in list------
					Global_Rename_List.append('Global_C')
					Global_Rename_List.append('Global_C_Offset')
					# Color of Global_C
					Plc = cmds.listRelatives('Global_C' , s=True)[0]
					cmds.setAttr(Plc + '.overrideEnabled', 1 )
					cmds.setAttr(Plc + '.overrideColor', 14 )
					# Connect Main and Global Ctrls
					cmds.parent('Main_C_Offset','Global_C')
					# Parent All existing ctrl groups under the Main_C
					cmds.parent( str(rig_name) + '_' + "Ctrl_Grp" , 'Main_C')
					# Making the placement control: This will have scaling locked
					v=n*2.2
					cmds.curve( n='Placement_C', d=1, p=[(-1.25*v, 0, -1.25*v),(-1.25*v, 0, -3.75*v), (-2.5*v, 0, -3.75*v),(0,0,-6.25*v),
						(2.5*v,0,-3.75*v),(1.25*v, 0, -3.75*v),(1.25*v, 0 ,-1.25*v),(3.75*v, 0, -1.25*v),(3.75*v,0,-2.5*v), (6.25*v ,0 ,0 ),
						(3.75*v, 0, 2.5*v),(3.75*v ,0 ,1.25*v), (1.25*v ,0, 1.25*v), (1.25*v ,0 ,3.75*v),(2.5*v, 0 ,3.75*v),(0 ,0, 6.25*v),
						(-2.5*v ,0, 3.75*v),(-1.25*v, 0 ,3.75*v),(-1.25*v, 0, 1.25*v),(-3.75*v, 0, 1.25*v),(-3.75*v ,0, 2.5*v ),
						(-6.25*v ,0 ,0 ),(-3.75*v, 0, -2.5*v),(-3.75*v ,0 ,-1.25*v ),( -1.25*v, 0, -1.25*v)])
					cmds.select( 'Placement_C.cv[0]','Placement_C.cv[6]','Placement_C.cv[12]','Placement_C.cv[18]','Placement_C.cv[24]' )
					cmds.scale( 1.57, 1.57, 1.57, r=True, ocp=True, xc='edge',a=True)
					cmds.select( 'Placement_C.cv[1:5]', 'Placement_C.cv[7:11]', 'Placement_C.cv[13:17]', 'Placement_C.cv[19:23]')
					cmds.scale( 0.6, 0.6, 0.6, r=True, ocp=True)  
					cmds.select(cl=True)
					rell = cmds.listRelatives( 'Placement_C', s=True)[0]
					cmds.setAttr( rell + '.overrideEnabled', 1 )
					cmds.setAttr( rell + '.overrideColor', 16 )

					cmds.select(cl=True)
					# Grouping the Placement_C and placing it above all ctrls
					cmds.group('Placement_C', n='Placement_C_Offset')
					cmds.group('Placement_C_Offset', n = str(rig_name) + '_' + "CTRL_SYSTEM")
					cmds.parent('Global_C_Offset', 'Placement_C')
					cmds.parent(str(rig_name) + '_' + "CTRL_SYSTEM" , str(rig_name) + '_' + 'RIG')

					# add in list------
					Global_Rename_List.append('Placement_C')
					Global_Rename_List.append('Placement_C_Offset')
					# Locking the scale of Placement_C
					cmds.setAttr( 'Placement_C.scaleX', lock=True, channelBox=False, k=False)
					cmds.setAttr( 'Placement_C.scaleY', lock=True, channelBox=False, k=False)
					cmds.setAttr( 'Placement_C.scaleZ', lock=True, channelBox=False, k=False)
					cmds.setAttr( 'Placement_C.visibility', lock=True, channelBox=False, k=False)

					cmds.setAttr('Global_C.visibility', lock=True, channelBox=False, k=False)
					# Adding Global_C Attributes
					if attr_01:
						cmds.addAttr('Global_C', longName= 'Global_Scale', at='float', dv=1.00, max=10.0, min=0.1, keyable=True)
						cmds.setAttr('Global_C.Global_Scale', cb=True, keyable=False)  
						print('Global Scale added')
						
					if attr_02:
						cmds.addAttr('Global_C', longName= 'Mesh_Display', at='enum', en= "normal:template:reference", keyable=True)
						cmds.setAttr('Global_C.Mesh_Display', cb=True, keyable=False)
						print('Mesh Display added')
					
					if attr_03:
						cmds.addAttr('Global_C', longName= 'Mesh_VIS', min=0, max=1, dv=1, keyable=True)
						cmds.setAttr('Global_C.Mesh_VIS', cb=True, keyable=False)
						print('Mesh VIS added')
						
					if attr_04:
						cmds.addAttr('Global_C', longName= 'Ctrl_VIS', min=0, max=1, dv=1, keyable=True)
						cmds.setAttr('Global_C.Ctrl_VIS', cb=True, keyable=False)
						print('Ctrl VIS added')
						
					if attr_05:
						cmds.addAttr('Global_C', longName= 'Jnt_VIS', min=0, max=1, dv=0, keyable=True)
						cmds.setAttr('Global_C.Jnt_VIS', cb=True, keyable=False)
						print('Jnt VIS added')
					
					# Connecting all Global Scale Attributes
					cmds.connectAttr('Global_C.Global_Scale', 'Global_C.scaleX')
					cmds.connectAttr('Global_C.Global_Scale', 'Global_C.scaleY')
					cmds.connectAttr('Global_C.Global_Scale', 'Global_C.scaleZ')

					cmds.setAttr('Global_C.scaleX', k=False, cb=False, l=True)
					cmds.setAttr('Global_C.scaleY', k=False, cb=False, l=True)
					cmds.setAttr('Global_C.scaleZ', k=False, cb=False, l=True)

					# Connecting Mesh Display with Override Display type
					cmds.setAttr(str(rig_name) + '_' + 'Mesh_Grp.overrideEnabled', 1)
					cmds.connectAttr('Global_C.Mesh_Display', str(rig_name) + '_' + 'Mesh_Grp.overrideDisplayType')
					
					# Setting default value to Reference, i.e. 2
					cmds.setAttr('Global_C.Mesh_Display', 2 )
					
					# Connecting Mesh_VIS
					cmds.connectAttr('Global_C.Mesh_VIS', str(rig_name) + '_' + 'Mesh_Grp.v')
					cmds.setAttr(str(rig_name) + '_' + 'Mesh_Grp.v', k=False, cb=True, l=True)
					
					# Connecting Ctrl_VIS
					cmds.connectAttr('Global_C.Ctrl_VIS', str(rig_name) + '_' + 'Ctrl_Grp.v')
					cmds.setAttr( str(rig_name) + '_' + 'Ctrl_Grp.v', k=False, cb=True, l=True)
					
					# Connecting Jnt_VIS
					cmds.connectAttr('Global_C.Jnt_VIS', str(rig_name) + '_' + 'Joint_Grp.v')
					cmds.setAttr(str(rig_name) + '_' + 'Joint_Grp.v', k=False, cb=True, l=True)

					# Finalising the RIG Group
					cmds.setAttr(str(rig_name) + '_' + 'RIG.translateX', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.translateY', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.translateZ', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.rotateX', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.rotateY', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.rotateZ', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.scaleX', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.scaleY', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.scaleZ', k=False, cb=False, l=True)
					cmds.setAttr(str(rig_name) + '_' + 'RIG.visibility', k=False, cb=True)
					# Lock and Hide Vis control of the Main_C
					cmds.setAttr('Main_C.visibility', k=False, cb=False, lock=True)

					# Lock and Hide of Visibility channel of the individual controls
					for ctrl in (cmds.ls('*_C')):
						cmds.setAttr( ctrl + ".v", k=False, cb=False, l=True)

					cmds.select(cl=True)
					
					for count, item in enumerate(Global_Rename_List):
						cmds.rename( item, str(rig_name) + '_' + item)
	
	else:
		# Joint is not provided, so it will loop through the given shapes and place the place the joints
		shapes_list = cmds.ls(sl=True)
		for item in shapes_list:
			# ===========================================================================================
			# Make a joint if not already provided:
			cmds.select(cl=True)
			Jnt = cmds.joint( n = item + '_Jnt')
			print(item, 'Joint Created')
			# ===========================================================================================
			# Joint Placement:
			if cmds.radioButton(ps_01, query=True, select=True):
				cmds.delete(cmds.parentConstraint(cmds.cluster(item, n='cls'), item + '_Jnt' ))
				cmds.delete('cls')
				
			elif cmds.radioButton(ps_02, query=True, select=True):
				cmds.delete(cmds.parentConstraint( item, item + '_Jnt'))

			# After the joint is placed we will delete history Freeze Transforms of the shape
			cmds.delete( item, constructionHistory=True)
			cmds.makeIdentity( item, t=1, r=1, s=1, apply=True )
			# ===========================================================================================
			# Make Controllers for every shape
			print('Radius: ', n)
			if current_shape == 'cube':
				cmds.curve(n= item + '_C', d=1, p=[(-n, n, n), (-n, -n, n),(n, -n, n),(n, n, n),(-n, n, n), 
				(-n, n, -n), (-n, -n, -n), (n, -n, -n), (n, n, -n), (-n, n, -n), (n, n, -n), (n, n, n), 
				(n, -n, n), (n, -n, -n), (-n, -n, -n), (-n, -n, n)]) 
				cmds.delete( item + '_C', constructionHistory=True)
				
			elif current_shape == 'circle':
				cmds.circle( radius=n, n= item + '_C')
				cmds.xform(item + '_C', ro=(-90,0,0), r=True, os=True)
				cmds.makeIdentity(item + '_C', apply=True, t=1, r=1, s=1)
				cmds.delete( item + '_C', constructionHistory=True)
				
			elif current_shape == 'square':
				cmds.curve(n= item + '_C', d=1, p=[(-n, 0, -n),(n,0,-n),(n,0,n),(-n,0,n),(-n,0,-n)])
				cmds.delete( item + '_C', constructionHistory=True)
				
			elif current_shape == 'triangle':
				cmds.curve(n= item + '_C', d=1, p=[(n,0,n),(-n,0,0),(n,0,-n),(n,0,n)] )
				cmds.delete( item + '_C', constructionHistory=True)
				
			elif current_shape == 'Hexagon':
				cmds.circle( name= item + '_C', radius=n, d=1, s=6)
				cmds.xform(item + '_C', ro=(90,0,0))
				cmds.makeIdentity(item + '_C', apply=True, t=1, s=1, r=1)
				cmds.delete( item + '_C', constructionHistory=True)
				
			elif current_shape == 'COG':
				m = n*0.5
				cmds.circle( radius=n, n= item + '_C')
				cmds.xform(item + '_C', ro=(90,0,0), r=True, os=True)
				cmds.makeIdentity( item + '_C', apply=True, t=1, r=1, s=1)
				cmds.curve( n='COG_C2', d=1, p=[(-1.25*m, 0, -1.25*m),(-1.25*m, 0, -3.75*m), (-2.5*m, 0, -3.75*m),
				(0,0,-6.25*m),(2.5*m,0,-3.75*m),(1.25*m, 0, -3.75*m),(1.25*m, 0 ,-1.25*m),(3.75*m, 0, -1.25*m),(3.75*m,0,-2.5*m), 
				(6.25*m ,0 ,0 ),(3.75*m, 0, 2.5*m),(3.75*m ,0 ,1.25*m), (1.25*m ,0, 1.25*m), (1.25*m ,0 ,3.75*m),(2.5*m, 0 ,3.75*m),
				(0 ,0, 6.25*m),(-2.5*m ,0, 3.75*m),(-1.25*m, 0 ,3.75*m),(-1.25*m, 0, 1.25*m),(-3.75*m, 0, 1.25*m),(-3.75*m ,0, 2.5*m ),
				(-6.25*m ,0 ,0 ), (-3.75*m, 0, -2.5*m),(-3.75*m ,0 ,-1.25*m ),( -1.25*m, 0, -1.25*m)])
				cmds.select( 'COG_C2.cv[0]','COG_C2.cv[6]','COG_C2.cv[12]','COG_C2.cv[18]','COG_C2.cv[24]' )
				cmds.scale( 1.57, 1.57, 1.57, r=True, ocp=True, xc='edge',a=True) 
				cmds.select(cl=True)
				rel = cmds.listRelatives( 'COG_C2', s=True)[0]

				cmds.setAttr( rel + '.overrideEnabled', 1 )
				cmds.setAttr( rel + '.overrideColor', col-1 )
				cmds.select( rel , item + '_C')
				cmds.parent (relative=True, s=True)
				cmds.delete('COG_C2')
				cmds.select(cl=True)

				cmds.delete( item + '_C', constructionHistory=True)
				
			elif current_shape == 'Plus':
				cmds.curve(n= item + '_C', d=1, p=[(n, 0 ,n ),( n, 0, 3*n),(-n, 0, 3*n),
				  (-n, 0, n),(-3*n, 0, n), (-3*n, 0, -n), (-n, 0, -n), (-n, 0, -3*n),
				  ( n, 0, -3*n),(n, 0, -n), (3*n, 0, -n), (3*n,0, n), (n, 0, n)] ) 
				cmds.delete( item + '_C', constructionHistory=True)
				
			elif current_shape == 'Arrow':
				m = n*0.5
				cmds.curve(n= item + '_C', d=1, p=[(-1.25*m, 0, 2.5*m), (-1.25*m,0,0), (-2.5*m,0,0),
				(0,0,-2.5*m),(2.5*m,0,0),(1.25*m,0,0),(1.25*m,0,2.5*m), (-1.25*m, 0,2.5*m)] )
				cmds.delete( item + '_C', constructionHistory=True)
				
			elif current_shape == 'locator':
				cmds.curve(n= item + '_C' ,d=1,p=[(0, 1.25*n, 0), (0, 0, 0), (0,-1.25*n, 0),(0,0,0),
				(1.25*n,0,0) ,(0,0,0),(-1.25*n,0,0),(0,0,0),(0,0,1.25*n),(0,0,0),(0,0,-1.25*n)] )  
				cmds.delete( item + '_C', constructionHistory=True)
				
			else:
				cmds.error('Invalid option!')
			# ===========================================================================================
			# Offset groups for controls
			cmds.group( item + '_C', n = item + '_C_Grp' )
			cmds.group( item + '_C_Grp', n = item + '_C_Grp1' )
			# ===========================================================================================
			# Positioning the controller groups	according to joint pos
			cmds.delete(cmds.parentConstraint( item + '_Jnt', item + '_C_Grp1' ))
			cmds.delete( item + '_Jnt', constructionHistory=True)
			cmds.makeIdentity( item + '_Jnt',t=1, r=1, s=1, apply=True)
			# ===========================================================================================
			# Constrain the Joints with their controls
			if pc==1:
				cmds.parentConstraint(item + '_C', item + '_Jnt' , mo=True)
				
			if sc==1:
				cmds.scaleConstraint(item + '_C', item + '_Jnt', mo=True )
				
			# ===========================================================================================
			# Color of controls (Assigning the colors to the controls)
			print('Color: ', col)
			shape_node = cmds.listRelatives(item + '_C' , s=True)[0]

			cmds.setAttr( shape_node + '.overrideEnabled', 1 )
			cmds.setAttr( shape_node + '.overrideColor', col-1 )
			cmds.select(cl=True)
			# ===========================================================================================
			# Add Skin Cluster to the shape (Skinning shapes to their respective joints)
			if cmds.radioButton(sk_01, query=True, select=True):
				cmds.skinCluster( item, item + '_Jnt' )
				
		#==================OPTION FOR MAKING AN OVERALL GROUP================================
		if make_grp==1:
			# Make groups for Geo, Jnts and Ctrls
			Ctrl_Grp_List = cmds.ls('*_C_Grp1')
			cmds.group(Ctrl_Grp_List, n="Ctrl_Grp")
			Jnt_Grp_List = cmds.ls('*_Jnt')
			cmds.group(Jnt_Grp_List, n="Joint_Grp")
			cmds.group(shapes_list, n="Mesh_Grp")
			cmds.group("Mesh_Grp","Joint_Grp","Ctrl_Grp", n="RIG")
			
			# Renaming the Overall Groups
			cmds.select("RIG", hierarchy = True)
			Rename_without_Global_List = cmds.ls(sl=True)
			
			# logic: sometimes shape nodes specifically might create problems, so we deselcent those first
			for obj in shapes_list:
				q = cmds.listRelatives(obj, s=True)
				cmds.select(q,d = True)
			New_without_shape_list = cmds.ls(sl=1)
			
			for count, item in enumerate(New_without_shape_list):
				if cmds.objExists(item):
					cmds.rename( item, str(rig_name) + '_' + item)
		else:
			print("Group option not selected")
		# --------------------------
		# Making a Global Ctrl
		if cmds.radioButton(gb_01, query=True, select=True):
			x = n*3
			cmds.curve(n= 'Main_C', d=1, p=[(-x, 0, -x),(x,0,-x),(x,0,x),(-x,0,x),(-x,0,-x)])
			cmds.group('Main_C', n= 'Main_C_Offset')
			cmds.select(cl=True)
			# Color of Main_C
			Glb = cmds.listRelatives('Main_C' , s=True)[0]
			cmds.setAttr(Glb + '.overrideEnabled', 1 )
			cmds.setAttr(Glb + '.overrideColor', 13 )

			# Making Global_C
			cmds.circle( r=n*5 , d=1, s=6, n= 'Global_C')
			cmds.xform('Global_C', ro=(90,0,0))
			cmds.makeIdentity('Global_C', apply=True, t=1, s=1, r=1)
			cmds.group('Global_C', n= 'Global_C_Offset')
			cmds.select(cl=True)
			
			# Color of Global_C
			Plc = cmds.listRelatives('Global_C' , s=True)[0]
			cmds.setAttr(Plc + '.overrideEnabled', 1 )
			cmds.setAttr(Plc + '.overrideColor', 14 )
			
			# Connect Main and Global Ctrls
			cmds.parent('Main_C_Offset','Global_C')
			
			# Parent All existing ctrl groups under the Main_C
			cmds.parent(str(rig_name) + '_' + "Ctrl_Grp", 'Main_C')
			
			# Making the placement control: This will have scaling locked
			v=n*2.2
			
			cmds.curve( n='Placement_C', d=1, p=[(-1.25*v, 0, -1.25*v),(-1.25*v, 0, -3.75*v), (-2.5*v, 0, -3.75*v),(0,0,-6.25*v),
				(2.5*v,0,-3.75*v),(1.25*v, 0, -3.75*v),(1.25*v, 0 ,-1.25*v),(3.75*v, 0, -1.25*v),(3.75*v,0,-2.5*v), (6.25*v ,0 ,0 ),
				(3.75*v, 0, 2.5*v),(3.75*v ,0 ,1.25*v), (1.25*v ,0, 1.25*v), (1.25*v ,0 ,3.75*v),(2.5*v, 0 ,3.75*v),(0 ,0, 6.25*v),
				(-2.5*v ,0, 3.75*v),(-1.25*v, 0 ,3.75*v),(-1.25*v, 0, 1.25*v),(-3.75*v, 0, 1.25*v),(-3.75*v ,0, 2.5*v ),
				(-6.25*v ,0 ,0 ),(-3.75*v, 0, -2.5*v),(-3.75*v ,0 ,-1.25*v ),( -1.25*v, 0, -1.25*v)])
			cmds.select( 'Placement_C.cv[0]','Placement_C.cv[6]','Placement_C.cv[12]','Placement_C.cv[18]','Placement_C.cv[24]' )
			cmds.scale( 1.57, 1.57, 1.57, r=True, ocp=True, xc='edge',a=True)
			cmds.select( 'Placement_C.cv[1:5]', 'Placement_C.cv[7:11]', 'Placement_C.cv[13:17]', 'Placement_C.cv[19:23]')
			cmds.scale( 0.6, 0.6, 0.6, r=True, ocp=True)  
			cmds.select(cl=True)
			
			rell = cmds.listRelatives( 'Placement_C', s=True)[0]
			
			cmds.setAttr( rell + '.overrideEnabled', 1 )
			cmds.setAttr( rell + '.overrideColor', 16 )
			
			cmds.select(cl=True)
			
			# Grouping the Placement_C and placing it above all ctrls
			cmds.group('Placement_C', n='Placement_C_Offset')
			cmds.group('Placement_C_Offset', n= str(rig_name) + '_' + "CTRL_SYSTEM")
			cmds.parent('Global_C_Offset', 'Placement_C')
			cmds.parent(str(rig_name) + '_' + "CTRL_SYSTEM" , str(rig_name) + '_' + 'RIG')
			
			# Locking the scale of Placement_C
			cmds.setAttr( 'Placement_C.scaleX', lock=True, channelBox=False, k=False)
			cmds.setAttr( 'Placement_C.scaleY', lock=True, channelBox=False, k=False)
			cmds.setAttr( 'Placement_C.scaleZ', lock=True, channelBox=False, k=False)
			cmds.setAttr( 'Placement_C.visibility', lock=True, channelBox=False, k=False)
			
			cmds.setAttr('Global_C.visibility', lock=True, channelBox=False, k=False)
			
			# Adding Global_C Attributes
			if attr_01:
				cmds.addAttr('Global_C', longName= 'Global_Scale', at='float', dv=1.00, max=10.0, min=0.1, keyable=True)
				cmds.setAttr('Global_C.Global_Scale', cb=True, keyable=False)  
				print('Global Scale added')
			
				
			if attr_02:
				cmds.addAttr('Global_C', longName= 'Mesh_Display', at='enum', en= "normal:template:reference", keyable=True)
				cmds.setAttr('Global_C.Mesh_Display', cb=True, keyable=False)
				print('Mesh Display added')
			
			
			if attr_03:
				cmds.addAttr('Global_C', longName= 'Mesh_VIS', min=0, max=1, dv=1, keyable=True)
				cmds.setAttr('Global_C.Mesh_VIS', cb=True, keyable=False)
				print('Mesh VIS added')
			
				
			if attr_04:
				cmds.addAttr('Global_C', longName= 'Ctrl_VIS', min=0, max=1, dv=1, keyable=True)
				cmds.setAttr('Global_C.Ctrl_VIS', cb=True, keyable=False)
				print('Ctrl VIS added')
			
				
			if attr_05:
				cmds.addAttr('Global_C', longName= 'Jnt_VIS', min=0, max=1, dv=0, keyable=True)
				cmds.setAttr('Global_C.Jnt_VIS', cb=True, keyable=False)
				print('Jnt VIS added')
			# Connecting all Global Scale Attributes
			cmds.connectAttr('Global_C.Global_Scale', 'Global_C.scaleX')
			cmds.connectAttr('Global_C.Global_Scale', 'Global_C.scaleY')
			cmds.connectAttr('Global_C.Global_Scale', 'Global_C.scaleZ')

			cmds.setAttr('Global_C.scaleX', k=False, cb=False, l=True)
			cmds.setAttr('Global_C.scaleY', k=False, cb=False, l=True)
			cmds.setAttr('Global_C.scaleZ', k=False, cb=False, l=True)

			# Connecting Mesh Display with Override Display type
			cmds.setAttr(str(rig_name) + '_' + 'Mesh_Grp.overrideEnabled', 1)
			cmds.connectAttr('Global_C.Mesh_Display', str(rig_name) + '_' + 'Mesh_Grp.overrideDisplayType')
			# Setting default value to Reference, i.e. 2
			cmds.setAttr('Global_C.Mesh_Display', 2 )
			# Connecting Mesh_VIS
			cmds.connectAttr('Global_C.Mesh_VIS', str(rig_name) + '_' + 'Mesh_Grp.v')
			cmds.setAttr(str(rig_name) + '_' + 'Mesh_Grp.v', k=False, cb=True, l=True)
			# Connecting Ctrl_VIS
			cmds.connectAttr('Global_C.Ctrl_VIS', str(rig_name) + '_' + 'Ctrl_Grp.v')
			cmds.setAttr(str(rig_name) + '_' + 'Ctrl_Grp.v', k=False, cb=True, l=True)
			# Connecting Jnt_VIS
			cmds.connectAttr('Global_C.Jnt_VIS', str(rig_name) + '_' + 'Joint_Grp.v')
			cmds.setAttr(str(rig_name) + '_' + 'Joint_Grp.v', k=False, cb=True, l=True)

			# Finalising the RIG Group
			cmds.setAttr(str(rig_name) + '_' + 'RIG.translateX', k=False, cb=False, l=True)
			cmds.setAttr(str(rig_name) + '_' + 'RIG.translateY', k=False, cb=False, l=True)
			cmds.setAttr(str(rig_name) + '_' + 'RIG.translateZ', k=False, cb=False, l=True)
			cmds.setAttr(str(rig_name) + '_' + 'RIG.rotateX', k=False, cb=False, l=True)
			cmds.setAttr(str(rig_name) + '_' + 'RIG.rotateY', k=False, cb=False, l=True)
			cmds.setAttr(str(rig_name) + '_' + 'RIG.rotateZ', k=False, cb=False, l=True)
			cmds.setAttr(str(rig_name) + '_' + 'RIG.scaleX', k=False, cb=False, l=True)
			cmds.setAttr(str(rig_name) + '_' + 'RIG.scaleY', k=False, cb=False, l=True)
			cmds.setAttr(str(rig_name) + '_' + 'RIG.scaleZ', k=False, cb=False, l=True)
			cmds.setAttr(str(rig_name) + '_' + 'RIG.visibility', k=False, cb=True)
			# Lock and Hide Vis control of the Main_C
			cmds.setAttr('Main_C.visibility', k=False, cb=False, lock=True)

			# Lock and Hide of Visibility channel of the individual controls
			for ctrl in (cmds.ls('*_C')):
				cmds.setAttr( ctrl + ".v", k=False, cb=False, l=True)

			cmds.select(cl=True)
			Global_rename_list = ['Main_C', 'Main_C_Offset', 'Global_C', 'Global_C_Offset', 'Placement_C', 'Placement_C_Offset']
			for count, item in enumerate(Global_rename_list):
				cmds.rename( item, str(rig_name) + '_' + item)

#________________________________________________________________________________________________________________________________
#################################################################################################################################