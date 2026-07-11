%global tl_name ketcindy
%global tl_revision 58661

Name:		texlive-%{tl_name}
Epoch:		1
Version:	20191225.0
Release:	%{tl_revision}.1
Summary:	macros for graphic generation and Cinderella plugin
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/ketcindy
License:	gpl3+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ketcindy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ketcindy.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(ketcindy.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
KETpic is a macro package designed for computer algebra systems (CAS) to
generate LaTeX source codes for high-quality mathematical artwork.
KETcindy is a plugin for Cinderella that allows to generate graphics
using KETpic. The generated code can be included in any LaTeX document.

