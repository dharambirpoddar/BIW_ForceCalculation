#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 15:23:06 2023

@author: ubuntu
"""

import numpy as np
import matplotlib.pyplot as plt 

##Param
rho=1.22
v1=4#m/s
N=36  # no of holes
TotalArea=0.13*0.08
a1=0.00011951 #large area
a2=0.00003049
ar=a1/a2 #>1
v2=a1*v1/a2
p_atm=101325 #pascal


##calcualtion
def force_x(ang):
  theta=(np.pi/180)*ang
  fx=-rho*v1*v1*TotalArea+rho*v2*v2*N*a2*((np.sin(theta))**2)
  return fx*1000/9.8
  
def force_y(ang):
  theta=(3.14/180)*ang
  #fy=40*[-rho*v2*v2*a2*sin(theta)*cos(theta)]
  fy=N*(-rho*v2*v2*a2*(np.sin(theta))*(np.cos(theta)))
  return fy*1000/9.8
  
def forceRev_y(ang):
    theta=(3.14/180)*ang
    frevY=-rho*v1*v1*TotalArea+(N*rho*(v1/ar)**2*a2*(np.cos(theta))**2)
    return frevY*1000/9.8

def forceRev_x(ang):
    theta=(3.14/180)*ang
    frevX=-(N*rho*(v1/ar)**2*a2*np.cos(theta)*(np.sin(theta)))
    return frevX*1000/9.8

#
def forceBK():
    forceBK=-0.5*rho*TotalArea*v1**2
    return forceBK*1000/9.8

#Gain coefficient measured

def cglt(fxff,fxbf,fxfp,fyff,fybf,fyfp):
    cgl=(abs(fybf-fyff)/forceBK())
    cgt=(abs(2*fxfp-fxbf-fxff)/forceBK())
    return print (cgl,cgt)


# =============================================================================
# print(f'force_x= {force_x(45)}','gram')
# print(f'force_y= {force_y(45)}','gram')
# print(f'forceRev_y={forceRev_y(45)}','gram')
# print(f'forceRev_x={forceRev_x(45)}','gram')
# print(f'Beckmark force={forceBK()}')
# print(f'cg={Cg(45)}')
# 
# =============================================================================
