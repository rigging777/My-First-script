import maya.cmds as cmds

def add_stetch_squash(sel):
    """
    @ add stretch squash controller. on selected poly objects.
    add lattice non linear etc etc.
    @ param sel(list): poly mesh objects list
    """
    if not sel:
        raise RuntimeError('Error:- no object to add stretch squash')
sel = cmds.ls(sl=True)        
for each in sel:
    cmds.makeIdentity(each, apply=True, t=1, r=1, s=1, n=0)
    myLattice = cmds.lattice(each, dv=(6,6,6),oc=True)
    myGroup = cmds.createNode('transform', n=each+'_RG')
    cmds.parent(myLattice[1], myLattice[2], myGroup)
    cmds.hide(myGroup)
    myStretchSquash = cmds.nonLinear(each, typ='squash', lowBound=-1, highBound=1)
    squash = cmds.rename(myStretchSquash[0], 'squash_'+each)
    squashHandle = cmds.rename(myStretchSquash[1], 'squash_'+each+'_handle')
    myGroup = cmds.createNode('transform', n='_RG')
    cmds.parent(squashHandle, myGroup)
    cmds.hide(myGroup)
    myCluster = cmds.cluster(each)
    ctrlGrp = cmds.createNode('transform',n=each+'_grp')
    myController = cmds.circle(nr=(0, 0, 1), c=(0, 0, 0), r=2, ch=False, n=each+'_CTRL')
    cmds.parent(myController[0], ctrlGrp)
    cmds.delete(cmds.parentConstraint(myCluster, ctrlGrp, mo=False))
    cmds.delete(myCluster)
    cmds.color(ud=1)
    cmds.setAttr(myController[0]+'.v',l=True, k=False, cb=False)
    cmds.setAttr(myController[0]+'.sx',l=True, k=False, cb=False)
    cmds.setAttr(myController[0]+'.sy',l=True, k=False, cb=False)
    cmds.setAttr(myController[0]+'.sz',l=True, k=False, cb=False)
    cmds.addAttr(myController[0], ln='STSQ', min=-10, max=10, dv=0, k=True)
    cmds.setDrivenKeyframe(squash+".factor", cd=myController[0]+".STSQ", dv=0, v=0)
    cmds.setDrivenKeyframe(squash+".factor", cd=myController[0]+".STSQ", dv=10, v=-1)
    cmds.setDrivenKeyframe(squash+".factor", cd=myController[0]+".STSQ", dv=-10, v=1)
    myStretchSquash = cmds.nonLinear(each, typ='squash', lowBound=0, highBound=3)
    squash = cmds.rename(myStretchSquash[0], 'squash_'+each)
    squashHandle = cmds.rename(myStretchSquash[1], 'squash_'+each+'_handle')
    myGroup = cmds.createNode('transform', n='_RG')
    cmds.parent(squashHandle, myGroup)
    cmds.setAttr(myGroup+'.ty',-1)
    cmds.hide(myGroup)
    myCluster = cmds.cluster(each)
    ctrlGrp = cmds.createNode('transform', n=each+'dnctrlgrp')
    myArrow = cmds.curve(d=1,p=[(1, 0, 2), (-1, 0, 2), (-1, 0, 0), (-2, 0, 0), (0, 0, -3), (2, 0, 0), (1, 0, 0), (1, 0, 2)])
    cmds.parent(myArrow, ctrlGrp)
    cmds.delete(cmds.parentConstraint(myCluster, ctrlGrp, mo=False))
    cmds.delete(myCluster)
    cmds.setAttr(ctrlGrp+'.rx',-90)
    cmds.setAttr(ctrlGrp+'.ry',90)
    cmds.setAttr(ctrlGrp+'.ty',10)
    cmds.setAttr(myArrow+'.tx',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.ty',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.rx',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.ry',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.rz',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.sx',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.sy',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.sz',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.v',l=True, k=False, cb=False)
    cmds.transformLimits( tz=(-2.5,2.5), etz=(True, True) )
    cmds.setDrivenKeyframe(squash+".factor", cd=myArrow+".tz", dv=0, v=0)
    cmds.setDrivenKeyframe(squash+".factor", cd=myArrow+".tz", dv=2.5, v=.5)
    cmds.setDrivenKeyframe(squash+".factor", cd=myArrow+".tz", dv=-2.5, v=-.5)
    myStretchSquash = cmds.nonLinear(each, typ='squash', lowBound=-3, highBound=0)
    squash = cmds.rename(myStretchSquash[0], 'squash_'+each)
    squashHandle = cmds.rename(myStretchSquash[1], 'squash_'+each+'_handle')
    myGroup = cmds.createNode('transform', n='_RG')
    cmds.parent(squashHandle, myGroup)
    cmds.setAttr(myGroup+'.ty',1)
    cmds.hide(myGroup)
    myCluster = cmds.cluster(each)
    upctrlGrp = cmds.createNode('transform', n=each+'upctrlGrp')
    myArrow = cmds.curve(d=1,p=[(1, 0, 2), (-1, 0, 2), (-1, 0, 0), (-2, 0, 0), (0, 0, -3), (2, 0, 0), (1, 0, 0), (1, 0, 2)])
    cmds.parent(myArrow, upctrlGrp)
    cmds.delete(cmds.parentConstraint(myCluster, upctrlGrp, mo=False))
    cmds.delete(myCluster)
    cmds.setAttr(upctrlGrp+'.rx',90)
    cmds.setAttr(upctrlGrp+'.ry',90)
    cmds.setAttr(upctrlGrp+'.ty',-6)
    cmds.setAttr(myArrow+'.tx',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.ty',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.rx',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.ry',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.rz',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.sx',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.sy',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.sz',l=True, k=False, cb=False)
    cmds.setAttr(myArrow+'.v',l=True, k=False, cb=False)
    cmds.transformLimits( tz=(-2.5,2.5), etz=(True, True) )
    cmds.setDrivenKeyframe(squash+".factor", cd=myArrow+".tz", dv=0, v=0)
    cmds.setDrivenKeyframe(squash+".factor", cd=myArrow+".tz", dv=2.5, v=.5)
    cmds.setDrivenKeyframe(squash+".factor", cd=myArrow+".tz", dv=-2.5, v=-.5)
    cmds.parent(myGroup,ctrlGrp,upctrlGrp,myController)