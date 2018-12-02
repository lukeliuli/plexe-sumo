#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# go to additional mode
netedit.additionalMode()

#select calibrator
netedit.changeAdditional("calibrator")

# create first calibrator
netedit.leftClick(referencePosition, 245, 140)

# create second calibrator
netedit.leftClick(referencePosition, 170, 270)

# go to inspect mode
netedit.inspectMode()

# inspect calibrator
netedit.leftClick(referencePosition, 300, 205)

# Change parameter id with a non valid value (Duplicated ID)
netedit.modifyAttribute(3, "calibrator_gneE3_0")

# Change parameter id with a non valid value (Invalid ID)
netedit.modifyAttribute(3, "Id with spaces")

# Change parameter id with a valid value
netedit.modifyAttribute(3, "correctID")

# Check undos and redos
netedit.undo(referencePosition, 3)
netedit.redo(referencePosition, 3)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)