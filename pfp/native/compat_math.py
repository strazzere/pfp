#!/usr/bin/env python
# encoding: utf-8

"""
This module of native functions is implemented for
compatability with 010 editor functions. Some of these functions
are nops, some are fully implemented.
"""

import sys

from pfp.native import native
import pfp.fields

# http://www.sweetscape.com/010editor/manual/FuncMath.htm

#double Abs( double x )
@native(name="Abs", ret=pfp.fields.Double)
def Abs(params, ctxt, scope, stream, coord):
	pass

#double Ceil( double x )
@native(name="Ceil", ret=pfp.fields.Double)
def Ceil(params, ctxt, scope, stream, coord):
	pass

#double Cos( double a )
@native(name="Cos", ret=pfp.fields.Double)
def Cos(params, ctxt, scope, stream, coord):
	pass

#double Exp( double x )
@native(name="Exp", ret=pfp.fields.Double)
def Exp(params, ctxt, scope, stream, coord):
	pass

#double Floor( double x)
@native(name="Floor", ret=pfp.fields.Double)
def Floor(params, ctxt, scope, stream, coord):
	pass

#double Log( double x )
@native(name="Log", ret=pfp.fields.Double)
def Log(params, ctxt, scope, stream, coord):
	pass

#double Max( double a, double b )
@native(name="Max", ret=pfp.fields.Double)
def Max(params, ctxt, scope, stream, coord):
	pass

#double Min( double a, double b)
@native(name="Min", ret=pfp.fields.Double)
def Min(params, ctxt, scope, stream, coord):
	pass

#double Pow( double x, double y)
@native(name="Pow", ret=pfp.fields.Double)
def Pow(params, ctxt, scope, stream, coord):
	pass

#int Random( int maximum )
@native(name="Random", ret=pfp.fields.Int)
def Random(params, ctxt, scope, stream, coord):
	pass

#double Sin( double a )
@native(name="Sin", ret=pfp.fields.Double)
def Sin(params, ctxt, scope, stream, coord):
	pass

#double Sqrt( double x )
@native(name="Sqrt", ret=pfp.fields.Double)
def Sqrt(params, ctxt, scope, stream, coord):
	pass

#data_type SwapBytes( data_type x )
@native(name="SwapBytes", ret=pfp.fields.Int)
def SwapBytes(params, ctxt, scope, stream, coord):
	pass

#double Tan( double a )
@native(name="Tan", ret=pfp.fields.Double)
def Tan(params, ctxt, scope, stream, coord):
	pass