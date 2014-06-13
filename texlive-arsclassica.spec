# revision 25466
# category Package
# catalog-ctan /macros/latex/contrib/arsclassica
# catalog-date 2012-02-21 16:05:39 +0100
# catalog-license lppl
# catalog-version 4.0.3
Name:		texlive-arsclassica
Version:	4.0.3
Release:	6
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
%{_texmfdistdir}/makeindex/arsclassica/classic.ist
%{_texmfdistdir}/tex/latex/arsclassica/arsclassica.sty
%doc %{_texmfdistdir}/doc/latex/arsclassica/ArsClassica.pdf
%doc %{_texmfdistdir}/doc/latex/arsclassica/ArsClassica.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/Bibliography.bib
%doc %{_texmfdistdir}/doc/latex/arsclassica/CHANGES
%doc %{_texmfdistdir}/doc/latex/arsclassica/Chapters/Code.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/Chapters/Fundamentals.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Abstract+Sommario.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Acknowledgements.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Bibliography.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Contents.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Index.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Titleback.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/FrontBackMatter/Titlepage.tex
%doc %{_texmfdistdir}/doc/latex/arsclassica/Graphics/Birds.jpg
%doc %{_texmfdistdir}/doc/latex/arsclassica/Graphics/Example_1.jpg
%doc %{_texmfdistdir}/doc/latex/arsclassica/Graphics/Example_2.jpg
%doc %{_texmfdistdir}/doc/latex/arsclassica/Graphics/Example_3.jpg
%doc %{_texmfdistdir}/doc/latex/arsclassica/Graphics/Example_4.jpg
%doc %{_texmfdistdir}/doc/latex/arsclassica/README
%doc %{_texmfdistdir}/doc/latex/arsclassica/arsclassica-settings.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar makeindex tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.0.3-1
+ Revision: 779416
- Update to latest release.

* Wed Feb 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 4.0-1
+ Revision: 772015
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.7-2
+ Revision: 749349
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.7-1
+ Revision: 717856
- texlive-arsclassica
- texlive-arsclassica
- texlive-arsclassica
- texlive-arsclassica
- texlive-arsclassica

