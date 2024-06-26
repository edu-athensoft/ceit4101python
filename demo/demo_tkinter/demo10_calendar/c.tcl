#############################################################################
# Generated by PAGE version 5.5f
#  in conjunction with Tcl version 8.6
#  Oct 07, 2020 07:45:51 PM PDT  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}
dmsg c.tcl starting tops = vTcl(tops)
#set vTcl(tops) .top34


if {!$vTcl(borrow) && !$vTcl(template)} {

set desc "-family {DejaVu Sans Mono} -size 14"
set vTcl(actual_gui_font_dft_desc) $desc
set vTcl(actual_gui_font_dft_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 14"
set vTcl(actual_gui_font_text_desc) $desc
set vTcl(actual_gui_font_text_name) [font create {*}$desc]
set desc "-family {DejaVu Sans Mono} -size 14"
set vTcl(actual_gui_font_fixed_desc) $desc
set vTcl(actual_gui_font_fixed_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_menu_desc) $desc
set vTcl(actual_gui_font_menu_name) [font create {*}$desc]
set desc "-family {DejaVu Sans} -size 12"
set vTcl(actual_gui_font_tooltip_desc) $desc
set vTcl(actual_gui_font_tooltip_name) [font create {*}$desc]
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) wheat
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #f4bcb2
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) wheat
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #b2c9f4
set vTcl(analog_color_p) #eaf4b2
set vTcl(analog_color_m) #f4bcb2
set vTcl(active_fg) #111111
set vTcl(actual_gui_menu_active_bg)  #d8d8d8
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(actual_autoalias) 1
set vTcl(actual_relative_placement) 0
set vTcl(mode) Absolute
set vTcl(w,wm,dflt,origin) 1
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
dmsg spot c create btop = $btop
    dpr btop    
}


proc vTclWindow.top34 {base} {
    global vTcl
    if {$base == ""} {
        set base .top34
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black
    wm focusmodel $top passive
    wm geometry $top 173x213
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 1
    wm maxsize $top 1905 1170
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Calendar"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    ttk::style configure Text -background $vTcl(actual_gui_bg)
    ttk::style configure Text -foreground $vTcl(actual_gui_fg)
    ttk::style configure Text -font "$vTcl(actual_gui_font_dft_desc)"
    text $top.tex35 \
        -background white -font TkFixedFont -foreground black -height 132 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #ddc8a1 \
        -selectforeground black -width 171 -wrap word
    $top.tex35 configure -font "TkFixedFont"
    $top.tex35 insert end text
    vTcl:DefineAlias "$top.tex35" "Text1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but36 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command last \
        -disabledforeground #b8a786 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Last
    vTcl:DefineAlias "$top.but36" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $top.cpd37 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command current \
        -disabledforeground #b8a786 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Current
    vTcl:DefineAlias "$top.cpd37" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $top.cpd38 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command next \
        -disabledforeground #b8a786 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Next
    vTcl:DefineAlias "$top.cpd38" "Button3" vTcl:WidgetProc "Toplevel1" 1
    button $top.cpd39 \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -command quit \
        -disabledforeground #b8a786 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -state active -text Quit
    vTcl:DefineAlias "$top.cpd39" "Button4" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tex35 \
        -in $top -x 0 -y 0 -width 173 -relwidth 0 -height 132 -relheight 0 \
        -anchor nw -bordermode ignore
    place $top.but36 \
        -in $top -x 2 -y 140 -width 51 -relwidth 0 -height 29 -relheight 0 \
        -anchor nw -bordermode ignore
    place $top.cpd37 \
        -in $top -x 55 -y 140 -width 63 -relwidth 0 -height 29 -relheight 0 \
        -anchor nw -bordermode ignore
    place $top.cpd38 \
        -in $top -x 120 -y 140 -width 51 -relwidth 0 -height 29 -relheight 0 \
        -anchor nw -bordermode ignore
    place $top.cpd39 \
        -in $top -x 10 -y 179 -width 154 -relwidth 0 -height 30 -relheight 0 \
        -anchor nw -bordermode ignore
    } ;# end vTcl:withBusyCursor

    vTcl:FireEvent $base <<Ready>>
}


set vTcl(btop) $btop
dpr:print_tree .
Window show .
# Window show .top34 $btop
dmsg bottom c.tcl tops = $vTcl(tops) 
Window show $vTcl(tops) $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

