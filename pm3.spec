Summary:	The Polytechnique Montreal Modula-3 distribution
Name:		pm3
Version:	1.1.13
Release:	1
Group:		Development/Languages/Modula3
Source0:	ftp://m3.polymtl.ca/pub/m3/targzip/%{name}-%{version}.tgz
Source1:	pm3-LINUXLIBC6
Source2:	pm3-COMMON
Patch0:		pm3-readline.patch
Patch1:		pm3-ncurses.patch
Patch2:		pm3-m3gdb.patch
CopyRight:	Open Source, mostly BSD like, some LGPL/GPL
URL:		http://m3.polymtl.ca/m3
# PM3 runs on several platforms but for Linux only on i386.
# Since RPM is mostly popular on Linux... let's stick to i386/Linux
ExclusiveArch:	%{ix86}
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Polytechnique Montreal Modula-3 distribution is based on the DEC SRC
Modula-3 programming environment.

Modula-3 is a systems programming language that descends from Mesa,
Modula-2, Cedar, and Modula-2+. It also resembles its cousins Object
Pascal, Oberon, and Euclid.

The goal of Modula-3 is to be as simple and safe as it can be while
meeting the needs of modern systems programmers. Instead of exploring new
features, they studied the features of the Modula family of languages
that have proven themselves in practice and tried to simplify them into
a harmonious language. They found that most of the successful features
were aimed at one of two main goals: greater robustness, and a simpler,
more systematic type system.

Modula-3 retains one of Modula-2's most successful features, the
provision for explicit interfaces between modules. It adds objects and
classes, exception handling, garbage collection, lightweight processes
(or threads), and the isolation of unsafe features.

A large number of platform independant libraries are available for easily
constructing distributed, graphical, multi-threaded applications

%package mtex
Summary:	mtex is used to produce both troff man pages and HTML pages from the same source
Group:		Development/Languages/Modula3/text

%description mtex
mtex is used to produce both troff man pages and HTML pages
from the same source

%package m3doc
Summary:	m3doc produces both html and latex/postscript from the same source
Group:		Development/Languages/Modula3/text/sgmltools

%description m3doc
m3doc produces both html and latex/postscript from the same source

%package m3coco
Summary:	Modula-3 LL(1) parser generator
Group:		Development/Languages/Modula3/language/parsing

%description m3coco
Modula-3 LL(1) parser generator

%package tempfiles
Summary:	Library to build tempfiles
Group:		Development/Languages/Modula3/libs

%description tempfiles
Library to build tempfiles

%package sgml
Summary:	SGML/XML parsing library
Group:		Development/Languages/Modula3/text/sgmltools

%description sgml
SGML/XML parsing library

%package m3tosgml
Summary:	Translate commented Modula-3 units into html files
Group:		Development/Languages/Modula3/text/sgmltools

%description m3tosgml
Translate commented Modula-3 units into html files

%package sgmlconv
Summary:	filter HTML files and convert HTML files to LaTeX
Group:		Development/Languages/Modula3/text/sgmltools

%description sgmlconv
filter HTML files and convert HTML files to LaTeX

%package sgmllinear
Summary:	Group several HTML files into a linear document
Group:		Development/Languages/Modula3/text/sgmltools

%description sgmllinear
Group several HTML files into a linear document

%package sgmltools
Summary:	SGML related tools
Group:		Development/Languages/Modula3/text

%description sgmltools
SGML related tools

%package m3textohtml
Summary:	Convert Modula-3 units from LaTeX markup to HTML markup
Group:		Development/Languages/Modula3/text/sgmltools

%description m3textohtml
Convert Modula-3 units from LaTeX markup to HTML markup

%package sgmlnormalize
Summary:	Convert a SGML file to its canonical form
Group:		Development/Languages/Modula3/text/sgmltools

%description sgmlnormalize
Convert a SGML file to its canonical form

%package sgmlstructure
Summary:	Show the tree structure of a SGML file
Group:		Development/Languages/Modula3/text/sgmltools

%description sgmlstructure
Show the tree structure of a SGML file

%package sgmltom3
Summary:	Convert back a Modula-3 unit from HTML to M3
Group:		Development/Languages/Modula3/text/sgmltools

%description sgmltom3
Convert back a Modula-3 unit from HTML to M3

%package sil
Summary:	Sil is a simple drawing program that runs on Windows/NT, Sample of native Windows programming in Modula-3
Group:		Development/Languages/Modula3/graphics

%description sil
Sil is a simple drawing program that runs on Windows/NT,
Sample of native Windows programming in Modula-3

%package m3middle
Summary:	Modula-3 compiler's IL definition
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3middle
Modula-3 compiler's IL definition

%package m3front
Summary:	Modula-3 compiler front-end
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3front
Modula-3 compiler front-end

%package m3linker
Summary:	Modula-3 prelinker
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3linker
Modula-3 prelinker

%package m3objfile
Summary:	Modula-3 object file writers
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3objfile
Modula-3 object file writers

%package m3back
Summary:	Linux ELF and Windows/NT x86 back-ends
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3back
Linux ELF and Windows/NT x86 back-ends

%package m3driver
Summary:	Modula-3 compiler driver
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3driver
Modula-3 compiler driver

%package m3staloneback
Summary:	Standalone back-end program like m3cc that uses m3back, used for testing
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3staloneback
Standalone back-end program like m3cc that uses m3back, used for testing

%package m3loader
Summary:	an experimental dynamic loader for Windows/NT
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3loader
an experimental dynamic loader for Windows/NT

%package m3quake
Summary:	The quake interpreter used by m3build
Group:		Development/Languages/Modula3/language

%description m3quake
The quake interpreter used by m3build

%package m3templates
Summary:	Quake builtin functions for m3build
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3templates
Quake builtin functions for m3build

%package m3-base
Summary:	The Modula-3 compiler
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3-base
The Modula-3 compiler

%package m3bootstrap
Summary:	Cross compiles bootstrap packages for other platforms
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3bootstrap
Cross compiles bootstrap packages for other platforms

%package m3export
Summary:	Export and compiles a new release of PM3 from the CVS repository
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3export
Export and compiles a new release of PM3 from the CVS repository

%package m3tests
Summary:	Tests for the Modula-3 compiler
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3tests
Tests for the Modula-3 compiler

%package cg-burs
Summary:	An experimental Modula-3 back-end that uses BURS
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description cg-burs
An experimental Modula-3 back-end that uses BURS

%package coverage
Summary:	A line-based coverage analyzer/profiler
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description coverage
A line-based coverage analyzer/profiler

%package m3gdb
Summary:	Modula-3 aware debugger based on gdb
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description m3gdb
Modula-3 aware debugger based on gdb

%package pp
Summary:	Modula-3 pretty-printer
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description pp
Modula-3 pretty-printer

%package m3totex
Summary:	Wraps Modula-3 source in enough TeX to make it printable
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description m3totex
Wraps Modula-3 source in enough TeX to make it printable

%package set
Summary:	A simple, generic Set interface.
Group:		Development/Languages/Modula3/libs

%description set
A simple, generic Set interface.

%package digraph
Summary:	A directed graph type, generic over the types labeling nodes and edges
Group:		Development/Languages/Modula3/libs

%description digraph
A directed graph type, generic over the types labeling nodes and edges

%package table-list
Summary:	an association-list-based, generic implementation of Table.T
Group:		Development/Languages/Modula3/libs

%description table-list
an association-list-based, generic implementation of Table.T

%package realgeometry
Summary:	Geometry package (Point, Rect, Path, ...) with REAL-valued coordinates
Group:		Development/Languages/Modula3/libs

%description realgeometry
Geometry package (Point, Rect, Path, ...) with REAL-valued coordinates

%package parseparams
Summary:	A library that helps parse command line arguments.
Group:		Development/Languages/Modula3/libs

%description parseparams
A library that helps parse command line arguments.

%package slisp
Summary:	A library containing a small Lisp interpreter
Group:		Development/Languages/Modula3/language

%description slisp
A library containing a small Lisp interpreter

%package m3where
Summary:	Search for modula-3 packages and files
Group:		Development/Languages/Modula3/language/modula3/m3compiler

%description m3where
Search for modula-3 packages and files

%package tcp
Summary:	Implements a Modula-3 interface to TCP sockets
Group:		Development/Languages/Modula3/network/tcplibs

%description tcp
Implements a Modula-3 interface to TCP sockets

%package web
Summary:	library for retrieving documents from the World Wide Web using an http proxy server.
Group:		Development/Languages/Modula3/network/www

%description web
library for retrieving documents from the World Wide Web
using an http proxy server.

%package m3tk
Summary:	Modula-3 abstract syntax tree (AST) toolkit
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description m3tk
Modula-3 abstract syntax tree (AST) toolkit

%package netobj
Summary:	The network objects runtime library
Group:		Development/Languages/Modula3/network/netobjects

%description netobj
The network objects runtime library

%package stable
Summary:	A library providing log-based persistent objects
Group:		Development/Languages/Modula3/database/stableobjects

%description stable
A library providing log-based persistent objects

%package X11
Summary:	Modula-3 interface to the X library
Group:		Development/Languages/Modula3/graphics/gr-libs

%description X11
Modula-3 interface to the X library

%package PEX
Summary:	Modula-3 interface to the PEX 3D graphics library
Group:		Development/Languages/Modula3/graphics/gr-libs

%description PEX
Modula-3 interface to the PEX 3D graphics library

%package opengl
Summary:	Modula-3 interface to the OpenGL 3D graphics library
Group:		Development/Languages/Modula3/graphics/gr-libs

%description opengl
Modula-3 interface to the OpenGL 3D graphics library

%package motif
Summary:	Modula-3 interface to the X/Motif library
Group:		Development/Languages/Modula3/graphics/gr-libs

%description motif
Modula-3 interface to the X/Motif library

%package tetris
Summary:	Modula-3 version of Tetris
Group:		Development/Languages/Modula3/graphics/games

%description tetris
Modula-3 version of Tetris

%package columns
Summary:	Modula-3 version of the PC game, columns
Group:		Development/Languages/Modula3/graphics/games

%description columns
Modula-3 version of the PC game, columns

%package ui
Summary:	This library, ui, implements the Trestle window-system toolkit
Group:		Development/Languages/Modula3/graphics/gr-libs

%description ui
This library, ui, implements the Trestle window-system toolkit

%package bicycle
Summary:	Library of playing card images
Group:		Development/Languages/Modula3/graphics/games

%description bicycle
Library of playing card images

%package solitaire
Summary:	Modula-3 version of SeaHaven towers
Group:		Development/Languages/Modula3/graphics/games

%description solitaire
Modula-3 version of SeaHaven towers

%package badbricks
Summary:	Modula-3 game similar to minesweeper, inspired by the crumbling facade of SRC's building
Group:		Development/Languages/Modula3/graphics/games

%description badbricks
Modula-3 game similar to minesweeper,
inspired by the crumbling facade of SRC's building

%package m3scan
Summary:	Simple Modula-3 lexical token scanner
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description m3scan
Simple Modula-3 lexical token scanner

%package m3tohtml
Summary:	Convert batches of Modula-3 source to interconnected HTML
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description m3tohtml
Convert batches of Modula-3 source to interconnected HTML

%package m3markup
Summary:	Parse Modula-3 source code and insert HTML markup
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description m3markup
Parse Modula-3 source code and insert HTML markup

%package m3tohtmlf
Summary:	Convert one Modula-3 source to an HTML file
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description m3tohtmlf
Convert one Modula-3 source to an HTML file

%package tcpextras
Summary:	Additions to the tcp library
Group:		Development/Languages/Modula3/network/tcplibs

%description tcpextras
Additions to the tcp library

%package m3browser
Summary:	HTTP server that provides WWW browsing of the installed Modula-3 system
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description m3browser
HTTP server that provides WWW browsing of the installed Modula-3 system

%package tcl
Summary:	Thin Modula-3 veneer on the TCL library (version 6.2)
Group:		Development/Languages/Modula3/language

%description tcl
Thin Modula-3 veneer on the TCL library (version 6.2)

%package dps
Summary:	Thin Modula-3 veneer on the display Postscript extensions to X
Group:		Development/Languages/Modula3/graphics/displayps

%description dps
Thin Modula-3 veneer on the display Postscript extensions to X

%package dpsslides
Summary:	Program to display postscript slides in X
Group:		Development/Languages/Modula3/graphics/displayps

%description dpsslides
Program to display postscript slides in X

%package vbtkit
Summary:	Large collection of useful window widgets
Group:		Development/Languages/Modula3/graphics/gr-libs

%description vbtkit
Large collection of useful window widgets

%package fours
Summary:	Modula-3 variants of the PC game, tetris
Group:		Development/Languages/Modula3/graphics/games

%description fours
Modula-3 variants of the PC game, tetris

%package showheap
Summary:	graphically display in real-time the state of each heap page
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description showheap
graphically display in real-time the state of each heap page

%package recordheap
Summary:	Program to capture a showheap trace
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description recordheap
Program to capture a showheap trace

%package replayheap
Summary:	Graphically display the log captured by recordheap
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description replayheap
Graphically display the log captured by recordheap

%package shownew
Summary:	Graphically display in real-time per-type allocations
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description shownew
Graphically display in real-time per-type allocations

%package showthread
Summary:	Graphically display in real-time the state of each thread
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description showthread
Graphically display in real-time the state of each thread

%package images
Summary:	Support for displaying bitmap images
Group:		Development/Languages/Modula3/graphics/gr-libs

%description images
Support for displaying bitmap images

%package jvideo
Summary:	Low-level interface to the J-video hardware, needed by videovbt
Group:		Development/Languages/Modula3/graphics/gr-libs

%description jvideo
Low-level interface to the J-video hardware, needed by videovbt

%package videovbt
Summary:	Window widget that displays live video images
Group:		Development/Languages/Modula3/graphics/gr-libs

%description videovbt
Window widget that displays live video images

%package formsvbtpixmaps
Summary:	Bitmaps, cursors and stuff used by formsvbt
Group:		Development/Languages/Modula3/graphics/forms

%description formsvbtpixmaps
Bitmaps, cursors and stuff used by formsvbt

%package formsvbt
Summary:	High-level language based on S-expressions that makes it easy to assemble VBTs (windows) using the TeX metaphors of boxes and glue
Group:		Development/Languages/Modula3/graphics/forms

%description formsvbt
High-level language based on S-expressions that makes it easy
to assemble VBTs (windows) using the TeX metaphors of boxes and glue

%package formsedit
Summary:	A 1-1/2 view GUI editor for FormsVBT expressions
Group:		Development/Languages/Modula3/graphics/forms

%description formsedit
A 1-1/2 view GUI editor for FormsVBT expressions

%package m3ide
Summary:	Simple integrated development environment based on emacs
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description m3ide
Simple integrated development environment based on emacs

%package fisheye
Summary:	A demo of fisheye views for graph browsing
Group:		Development/Languages/Modula3/graphics/gr-libs

%description fisheye
A demo of fisheye views for graph browsing

%package calculator
Summary:	A 10-key calculator using FormsVBT
Group:		Development/Languages/Modula3/graphics/games

%description calculator
A 10-key calculator using FormsVBT

%package cube
Summary:	A rotating cube
Group:		Development/Languages/Modula3/graphics/games

%description cube
A rotating cube

%package board
Summary:	A network object graphical board
Group:		Development/Languages/Modula3/graphics/sharedboard

%description board
A network object graphical board

%package codeview
Summary:	Support for animated views of source code
Group:		Development/Languages/Modula3/graphics/animation

%description codeview
Support for animated views of source code

%package rehearsecode
Summary:	Program to manually test drive source code animations
Group:		Development/Languages/Modula3/graphics/animation

%description rehearsecode
Program to manually test drive source code animations

%package mg
Summary:	Low-level animation support
Group:		Development/Languages/Modula3/graphics/animation

%description mg
Low-level animation support

%package mgkit
Summary:	Collection of easier-to-use animation widgets
Group:		Development/Languages/Modula3/graphics/animation

%description mgkit
Collection of easier-to-use animation widgets

%package anim3D
Summary:	Collection of 3D animation widgets
Group:		Development/Languages/Modula3/graphics/animation

%description anim3D
Collection of 3D animation widgets

%package synloc
Summary:	Library for syntaxic analysis
Group:		Development/Languages/Modula3/language/parsing/metasyntax

%description synloc
Library for syntaxic analysis

%package synex
Summary:	Extensions to synloc
Group:		Development/Languages/Modula3/language/parsing/metasyntax

%description synex
Extensions to synloc

%package metasyn
Summary:	Meta syntax for synex
Group:		Development/Languages/Modula3/language/parsing/metasyntax

%description metasyn
Meta syntax for synex

%package obliq
Summary:	The Obliq interpreter
Group:		Development/Languages/Modula3/language/m3obliq

%description obliq
The Obliq interpreter

%package sgmlobliq
Summary:	Integrate the sgml library to Obliq
Group:		Development/Languages/Modula3/text/sgmltools

%description sgmlobliq
Integrate the sgml library to Obliq

%package m3zume
Summary:	The interesting event preprocessor needed by zeus
Group:		Development/Languages/Modula3/graphics/animation

%description m3zume
The interesting event preprocessor needed by zeus

%package zeus
Summary:	The algorithm animation toolkit
Group:		Development/Languages/Modula3/graphics/animation

%description zeus
The algorithm animation toolkit

%package mentor
Summary:	A collection of algoritm animations
Group:		Development/Languages/Modula3/graphics/animation

%description mentor
A collection of algoritm animations

%package smalldb
Summary:	In-memory database library, used by the package tools
Group:		Development/Languages/Modula3/database

%description smalldb
In-memory database library, used by the package tools

%package pkgtool
Summary:	client program(s) to access the package tools
Group:		Development/Languages/Modula3/network/pkgserver

%description pkgtool
client program(s) to access the package tools

%package visualobliq
Summary:	Prototype of an easy-to-use distributed programming environment
Group:		Development/Languages/Modula3/language/m3obliq

%description visualobliq
Prototype of an easy-to-use distributed programming environment

%package voquery
Summary:	A simple query program used by vorun
Group:		Development/Languages/Modula3/language/m3obliq

%description voquery
A simple query program used by vorun

%package vorun
Summary:	A safe visual obliq interpreter suitable for embedding in the WWW
Group:		Development/Languages/Modula3/language/m3obliq

%description vorun
A safe visual obliq interpreter suitable for embedding in the WWW

%package vocgi
Summary:	An HTML/cgi gateway, required to embed Visual Obliq code in the WWW
Group:		Development/Languages/Modula3/language/m3obliq

%description vocgi
An HTML/cgi gateway, required to embed Visual Obliq code in the WWW

%package llscan
Summary:	A little mh program used by Postcard
Group:		Development/Languages/Modula3/network/mail

%description llscan
A little mh program used by Postcard

%package postcard
Summary:	An integrated mail/news reader
Group:		Development/Languages/Modula3/network/mail

%description postcard
An integrated mail/news reader

%package gnuemacs
Summary:	A library of useful E-lisp code for Modual-3-mode in gnuemacs, also a program to build Modula-3 tags
Group:		Development/Languages/Modula3/language/modula3/m3tools

%description gnuemacs
A library of useful E-lisp code for Modual-3-mode in gnuemacs,
also a program to build Modula-3 tags

%package webvbt
Summary:	A library for displaying HTML pages inside a VBT
Group:		Development/Languages/Modula3/network/www

%description webvbt
A library for displaying HTML pages inside a VBT

%package webscape
Summary:	A web browser with support for interactive content
Group:		Development/Languages/Modula3/network/www

%description webscape
A web browser with support for interactive content

%package deckscape
Summary:	A web browser that uses a new metaphor: decks of web pages
Group:		Development/Languages/Modula3/network/www

%description deckscape
A web browser that uses a new metaphor: decks of web pages

%package webcard
Summary:	An integrated mail/news/web client
Group:		Development/Languages/Modula3/network/www

%description webcard
An integrated mail/news/web client

%package ocr
Summary:	Interface to optical character recognition library (DECstation only)
Group:		Development/Languages/Modula3/graphics/lecternpkg

%description ocr
Interface to optical character recognition library (DECstation only)

%package lectern
Summary:	The virtual paper document viewer
Group:		Development/Languages/Modula3/graphics/lecternpkg

%description lectern
The virtual paper document viewer

%package http
Summary:	Library for hypertext transfer protocol (HTTP)
Group:		Development/Languages/Modula3/network/www

%description http
Library for hypertext transfer protocol (HTTP)

%package webcat
Summary:	Program that takes a URL and prints out the web document
Group:		Development/Languages/Modula3/network/www

%description webcat
Program that takes a URL and prints out the web document

%package m3intro
Summary:	Introduction and documentation for Polytechnique Montreal Modula-3
Group:		Development/Languages/Modula3/.

%description m3intro
Introduction and documentation for Polytechnique Montreal Modula-3

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
install -m644 %{SOURCE1} m3config/src/LINUXLIBC6
install -m644 %{SOURCE2} m3config/src/COMMON
rm -rf $RPM_BUILD_ROOT

%build
%ifos linux
%ifarch %{ix86}

make -f Makefile.LINUXLIBC6 \
	M3OPTIONS="-DLIST_FILES -DSETROOT=%{_prefix} -DEXPORTPATH=$RPM_BUILD_ROOT"
%endif
%else
make \
	M3OPTIONS="-DLIST_FILES -DSETROOT=%{_prefix} -DEXPORTPATH=$RPM_BUILD_ROOT"
%endif

%install
make nothing

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/* || :
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/m3/i386-pld-linux/m3cgc1
strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/m3/pkg/*/LINUXLIBC6/*.so || :

#gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man{1,6}/*

cd files
for i in * ; do
	mv -f $i $i.bak
	sed -e 's/\(man\/man[0-9]\/.*\.[0-9]\)/\1\.gz/' $i.bak > $i
done

%files rehearsecode -f files/rehearsecode
%docdir /usr/lib/m3/www

%files webscape -f files/webscape
%docdir /usr/lib/m3/www

%files m3tosgml -f files/m3tosgml
%docdir /usr/lib/m3/www

%files dps -f files/dps
%docdir /usr/lib/m3/www

%files m3ide -f files/m3ide
%docdir /usr/lib/m3/www

%files m3staloneback -f files/m3staloneback
%docdir /usr/lib/m3/www

%files metasyn -f files/metasyn
%docdir /usr/lib/m3/www

%files sgmlstructure -f files/sgmlstructure
%docdir /usr/lib/m3/www

%files m3coco -f files/m3coco
%docdir /usr/lib/m3/www

%files tcp -f files/tcp
%docdir /usr/lib/m3/www

%files formsvbtpixmaps -f files/formsvbtpixmaps
%docdir /usr/lib/m3/www

%files m3linker -f files/m3linker
%docdir /usr/lib/m3/www

%files tetris -f files/tetris
%docdir /usr/lib/m3/www

%files pkgtool -f files/pkgtool
%docdir /usr/lib/m3/www

%files m3gdb -f files/m3gdb
%docdir /usr/lib/m3/www

%files realgeometry -f files/realgeometry
%docdir /usr/lib/m3/www

%files showthread -f files/showthread
%docdir /usr/lib/m3/www

%files codeview -f files/codeview
%docdir /usr/lib/m3/www

%files tcl -f files/tcl
%docdir /usr/lib/m3/www

%files ui -f files/ui
%docdir /usr/lib/m3/www

%files mtex -f files/mtex
%docdir /usr/lib/m3/www

%files lectern -f files/lectern
%docdir /usr/lib/m3/www

%files m3totex -f files/m3totex
%docdir /usr/lib/m3/www

%files showheap -f files/showheap
%docdir /usr/lib/m3/www

%files llscan -f files/llscan
%docdir /usr/lib/m3/www

%files m3markup -f files/m3markup
%docdir /usr/lib/m3/www

%files motif -f files/motif
%docdir /usr/lib/m3/www

%files mg -f files/mg
%docdir /usr/lib/m3/www

%files deckscape -f files/deckscape
%docdir /usr/lib/m3/www

%files sgmlconv -f files/sgmlconv
%docdir /usr/lib/m3/www

%files fisheye -f files/fisheye
%docdir /usr/lib/m3/www

%files visualobliq -f files/visualobliq
%docdir /usr/lib/m3/www

%files sgmltom3 -f files/sgmltom3
%docdir /usr/lib/m3/www

%files m3zume -f files/m3zume
%docdir /usr/lib/m3/www

%files m3export -f files/m3export
%docdir /usr/lib/m3/www

%files m3objfile -f files/m3objfile
%docdir /usr/lib/m3/www

%files m3-base -f files/m3-base
%docdir /usr/lib/m3/www

%files http -f files/http
%docdir /usr/lib/m3/www

%files parseparams -f files/parseparams
%docdir /usr/lib/m3/www

%files images -f files/images
%docdir /usr/lib/m3/www

%files opengl -f files/opengl
%docdir /usr/lib/m3/www

%files X11 -f files/X11
%docdir /usr/lib/m3/www

%files m3tk -f files/m3tk
%docdir /usr/lib/m3/www

%files bicycle -f files/bicycle
%docdir /usr/lib/m3/www

%files set -f files/set
%docdir /usr/lib/m3/www

%files recordheap -f files/recordheap
%docdir /usr/lib/m3/www

%files sgmlobliq -f files/sgmlobliq
%docdir /usr/lib/m3/www

%files m3tohtmlf -f files/m3tohtmlf
%docdir /usr/lib/m3/www

%files mgkit -f files/mgkit
%docdir /usr/lib/m3/www

%files webcard -f files/webcard
%docdir /usr/lib/m3/www

%files sgmllinear -f files/sgmllinear
%docdir /usr/lib/m3/www

%files dpsslides -f files/dpsslides
%docdir /usr/lib/m3/www

%files calculator -f files/calculator
%docdir /usr/lib/m3/www

%files voquery -f files/voquery
%docdir /usr/lib/m3/www

%files obliq -f files/obliq
%docdir /usr/lib/m3/www

%files sil -f files/sil
%docdir /usr/lib/m3/www

%files PEX -f files/PEX
%docdir /usr/lib/m3/www

%files zeus -f files/zeus
%docdir /usr/lib/m3/www

%files m3back -f files/m3back
%docdir /usr/lib/m3/www

%files coverage -f files/coverage
%docdir /usr/lib/m3/www

%files stable -f files/stable
%docdir /usr/lib/m3/www

%files m3templates -f files/m3templates
%docdir /usr/lib/m3/www

%files slisp -f files/slisp
%docdir /usr/lib/m3/www

%files webcat -f files/webcat
%docdir /usr/lib/m3/www

%files jvideo -f files/jvideo
%docdir /usr/lib/m3/www

%files m3middle -f files/m3middle
%docdir /usr/lib/m3/www

%files cg-burs -f files/cg-burs
%docdir /usr/lib/m3/www

%files netobj -f files/netobj
%docdir /usr/lib/m3/www

%files solitaire -f files/solitaire
%docdir /usr/lib/m3/www

%files m3doc -f files/m3doc
%docdir /usr/lib/m3/www

%files digraph -f files/digraph
%docdir /usr/lib/m3/www

%files replayheap -f files/replayheap
%docdir /usr/lib/m3/www

%files postcard -f files/postcard
%docdir /usr/lib/m3/www

%files m3bootstrap -f files/m3bootstrap
%docdir /usr/lib/m3/www

%files tcpextras -f files/tcpextras
%docdir /usr/lib/m3/www

%files anim3D -f files/anim3D
%docdir /usr/lib/m3/www

%files ocr -f files/ocr
%docdir /usr/lib/m3/www

%files vbtkit -f files/vbtkit
%docdir /usr/lib/m3/www

%files sgmltools -f files/sgmltools
%docdir /usr/lib/m3/www

%files cube -f files/cube
%docdir /usr/lib/m3/www

%files m3quake -f files/m3quake
%docdir /usr/lib/m3/www

%files vorun -f files/vorun
%docdir /usr/lib/m3/www

%files m3scan -f files/m3scan
%docdir /usr/lib/m3/www

%files mentor -f files/mentor
%docdir /usr/lib/m3/www

%files webvbt -f files/webvbt
%docdir /usr/lib/m3/www

%files m3tests -f files/m3tests
%docdir /usr/lib/m3/www

%files sgml -f files/sgml
%docdir /usr/lib/m3/www

%files m3driver -f files/m3driver
%docdir /usr/lib/m3/www

%files formsedit -f files/formsedit
%docdir /usr/lib/m3/www

%files synex -f files/synex
%docdir /usr/lib/m3/www

%files sgmlnormalize -f files/sgmlnormalize
%docdir /usr/lib/m3/www

%files m3intro -f files/m3intro
%docdir /usr/lib/m3/www

%files m3where -f files/m3where
%docdir /usr/lib/m3/www

%files videovbt -f files/videovbt
%docdir /usr/lib/m3/www

%files m3front -f files/m3front
%docdir /usr/lib/m3/www

%files m3loader -f files/m3loader
%docdir /usr/lib/m3/www

%files badbricks -f files/badbricks
%docdir /usr/lib/m3/www

%files table-list -f files/table-list
%docdir /usr/lib/m3/www

%files shownew -f files/shownew
%docdir /usr/lib/m3/www

%files gnuemacs -f files/gnuemacs
%docdir /usr/lib/m3/www

%files tempfiles -f files/tempfiles
%docdir /usr/lib/m3/www

%files m3browser -f files/m3browser
%docdir /usr/lib/m3/www

%files web -f files/web
%docdir /usr/lib/m3/www

%files formsvbt -f files/formsvbt
%docdir /usr/lib/m3/www

%files columns -f files/columns
%docdir /usr/lib/m3/www

%files synloc -f files/synloc
%docdir /usr/lib/m3/www

%files pp -f files/pp
%docdir /usr/lib/m3/www

%files fours -f files/fours
%docdir /usr/lib/m3/www

%files m3textohtml -f files/m3textohtml
%docdir /usr/lib/m3/www

%files board -f files/board
%docdir /usr/lib/m3/www

%files vocgi -f files/vocgi
%docdir /usr/lib/m3/www

%files m3tohtml -f files/m3tohtml
%docdir /usr/lib/m3/www

%files smalldb -f files/smalldb
%docdir /usr/lib/m3/www
