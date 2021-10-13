boolean show_grid;
show_grid := false;

pen outer_pen, inner_pen, grid_pen;
outer_pen := pencircle scaled 1bp yscaled 0.2 rotated 30;
inner_pen := pencircle scaled 0.7bp yscaled 0.2 rotated 30;
grid_pen := pencircle scaled 0.2bp;

def tr(expr s, ys, dx, dy) = scaled (s) yscaled ys shifted (dx, dy) enddef;

def clear(expr p) = fill buildcycle(p) withcolor .8white; enddef;

def box(expr xa, ya, xb, yb, r) =
  ((xa, yb-r) {up} .. {right} (xa+r, yb) ..
  (xb-r, yb) {right} .. {down} (xb, yb-r) ..
  (xb, ya+r) {down} .. {left} (xb-r, ya) ..
  (xa+r, ya) {left} .. {up} (xa, ya+r) .. cycle)
enddef;

def sq =
image(
  if show_grid:
    for a = -10 step 5 until 10:
      draw (a, -10) -- (a, 10) withpen grid_pen withcolor .5white;
      draw (-10, a) -- (10, a) withpen grid_pen withcolor .5white;
    endfor;
  fi;
)
enddef;

def logo_jan(expr s, ys, dx, dy) =
  image(
    path jan_a, jan_b;
    jan_a = box(-8, 0, 8, 10, 4) tr(s, ys, dx, dy);
    clear(jan_a)
    pickup outer_pen;
    draw jan_a;
    jan_b = (
      (0, 8) .. {down} (2.5, 2) {dir -20} .. tension 0.8 .. (10, -5) .. (5, -10) {left} 
      .. {left} (-5, -10) .. (-10, -5) .. tension 0.8 .. {dir 20} (-2.5, 2) {up} .. cycle
    ) tr(s, ys, dx, dy);
    clear(jan_b);
    draw jan_b;
    pickup inner_pen;
    draw ((-2.5, 2) {down} .. {right} (-2, 1.5) .. tension 0.8 .. {dir 100} (0.5, 6) ) tr(s, ys, dx, dy);
    draw fullcircle scaled 0.5 shifted(-1, 5) tr(s, ys, dx, dy);
    path jan_c, jan_d;
    jan_c := (-2, -2) -- (3, -5);
    jan_d := (2, -2) -- (-3, -5);
    draw jan_c tr(s, ys, dx, dy);
    draw jan_c shifted (-1, -1) tr(s, ys, dx, dy);
    draw jan_d tr(s, ys, dx, dy);
    draw jan_d shifted (1, -1) tr(s, ys, dx, dy);
    draw sq tr(s, ys, dx, dy);
  );
enddef;

def logo_mi(expr s, ys, dx, dy) =
  image (
    path mi_a, mi_b, mi_c;
    mi_a := box(-10, -10, 10, 10, 2);
    mi_b := box(-8, -6, 8, 6, 0.5);
    mi_c := fullcircle scaled 10;
    clear(mi_a tr(s, ys, dx, dy));
    draw sq tr(s, ys, dx, dy);
    draw mi_a tr(s, ys, dx, dy) withpen outer_pen;
    draw mi_b tr(s, ys, dx, dy) withpen inner_pen;
    draw mi_c tr(s, ys, dx, dy) withpen inner_pen;
  )
enddef;

def logo_moku(expr s, ys, dx, dy) =
  image (
    path moku_a;
    moku_a := 
      (0, 10) .. (-10, 0) {down} .. (-6, -10) {right} .. {up} (-3, -6) {down} ..
      {right} (0, -10) {right} .. {up} (3, -6) {down} .. {right} (6, -10) ..
      {up} (10, 0) .. cycle;
    moku_a := moku_a rotated 180;
    clear(moku_a tr(s, ys, dx, dy));
    draw sq tr(s, ys, dx, dy);
    draw moku_a tr(s, ys, dx, dy) withpen outer_pen;
  )  
enddef;

def logo_pona(expr s, ys, dx, dy) =
  image(
    path pona_a;
    pona_a := ((-8, 4) {dir 135}  .. (-6, 10) {right} .. {down} (-3, 6) {up} .. {down} (3, 6) {up} .. {right} (6, 10) ..
      {down} (10, 0) .. (0, -10) .. {up} (-10, 0) .. {dir 20} cycle) tr(s, ys, dx, dy);
    clear(pona_a);
    pickup outer_pen;
    draw pona_a;
    pickup inner_pen
    draw ((-8, 4) {dir 20} .. (0, 3) .. (6, 4)) tr(s, ys, dx, dy);
    draw ((-6, 1) .. (0, 0) .. (6, 1) .. (0, -5) .. cycle) tr(s, ys, dx, dy);
    draw ((-4, -1) .. (0, -3) .. (4, -1)) tr(s, ys, dx, dy);
  )
enddef;

def logo_telo(expr s, ys, dx, dy) =
  image (
    path telo_a, telo_b, telo_c, telo_d;
    telo_a :=
      (-10, -10) {dir 45} .. {right} (7, -10) .. tension 1.5 .. (7, -2);
    telo_b :=
      (-10, -10) {dir 60} .. {right} (7, -2) .. (8, 4);
    telo_c :=
      (-10, -10) {dir 80} .. tension 0.8 .. {right} (8, 4) .. (8, 9) .. (0, 7);
    telo_d :=
      (-10, -10) {up} .. {right} (-3, 9) .. (0, 7) .. (2, 6) .. (6, 7) ..
      {curl 0} (2, 6);
    clear((telo_a .. {down} cycle) tr(s, ys, dx, dy));
    clear((telo_b .. {down} cycle) tr(s, ys, dx, dy));
    clear((telo_c .. {down} cycle) tr(s, ys, dx, dy));
    clear((telo_d .. {down} cycle) tr(s, ys, dx, dy));
    draw sq tr(s, ys, dx, dy);
    pickup outer_pen;
    draw telo_a tr(s, ys, dx, dy);
    draw telo_b tr(s, ys, dx, dy);
    draw telo_c tr(s, ys, dx, dy);
    draw telo_d tr(s, ys, dx, dy);
  )
enddef;

def logo_toki(expr s, ys, dx, dy) =
  image (
    path toki_a;
    toki_a =
      ((0,10) .. (10, 5) .. {dir 200} (7, 2) {dir -60} .. (7, -7) .. (-1, -10) .. (-10, -5) {up} .. {up} (-10, 5) .. cycle) tr(s, ys, dx, dy);
    clear(toki_a);
    draw toki_a withpen outer_pen;
    pickup inner_pen;
    path toki_b, toki_c, toki_d, toki_e;
    toki_b := (7, 2) {dir 200} .. {curl 0.2} (-2, 3);
    draw toki_b tr(s, ys, dx, dy);
    toki_c := (3, 4) .. (6, -2) .. (3, -7) .. (-1, -2) .. cycle;
    toki_c := toki_c cutbefore toki_b;
    toki_c := toki_c cutafter toki_b;
    draw toki_c tr(s, ys, dx, dy);
    toki_d := (-2, -1) {right} .. (7, 0);
    toki_e := toki_d shifted (0, -2);
    toki_d := toki_d cutafter toki_c;
    toki_d := toki_d cutbefore toki_c;
    toki_e := toki_e cutafter toki_c;
    pair q;
    q := toki_c intersectionpoint toki_e;
    toki_e := toki_e cutafter q;
    draw toki_d tr(s, ys, dx, dy);
    draw toki_e tr(s, ys, dx, dy);
    draw (fullcircle scaled 3 shifted (-5, 5)) tr(s, ys, dx, dy);
    draw (fullcircle scaled 0.3 shifted (-5, 5)) tr(s, ys, dx, dy);
  )
enddef;

beginfig(1);
draw logo_jan(1, 1, 0, 0);
draw logo_mi(1, 1, 25, 0);
draw logo_moku(1, 1, 50, 0);
draw logo_pona(1, 1, 75, 0);
draw logo_telo(1, 1, 100, 0);
draw logo_toki(1, 1, 125, 0);
endfig;
end;
