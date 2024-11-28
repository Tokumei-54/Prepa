type graphe_bip = { n0: int; n1: int; aretes: (int*int) list }
type graphe = { mat_adj: int array array; s_adj: bool array; t_adj: bool array }

let g_bip_fig1 = { n0 = 6; n1 = 5; aretes = [(0,0);(0,1);(0,2);(0,4);(1,0);(2,0);(2,4);(3,0);(3,4);(4,4);(5,0);(5,2);(5,3);(5,4)] }

let make_graphe g = { 
  mat_adj = Array.make_matrix g.n0 g.n1 0 ;
  s_adj = Array.make g.n0 false;
  t_adj = Array.make g.n1 false }

let test = make_graphe g_bip_fig1

