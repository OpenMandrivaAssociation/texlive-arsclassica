Name:		texlive-arsclassica
Version:	20180303
Release:	2
Summary:	A different view of the ClassicThesis package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/arsclassica
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arsclassica.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/arsclassica.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package changes some typographical points of the
ClassicThesis style, by Andre Miede. It enables the user to
reproduce the look of the guide The art of writing with LaTeX
(the web page is in Italian).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tlpkg/tlpobj/arsclassica*
%{_texmfdistdir}/tex/latex/arsclassica
%doc %{_texmfdistdir}/doc/latex/arsclassica

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tlpkg tex doc %{buildroot}%{_texmfdistdir}
