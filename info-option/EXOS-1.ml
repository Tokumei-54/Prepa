(*Exercice 1.1*)

(*a*) 
let x = 2.
let y = let x_2 = x *. x in let x_4 = x_2 *. x_2 in x_4 *. x_4

(*b*)
let a_0 = let e_0 = 8.85418782e-12 and h_ = 1.054571818e-34 and m_e = 9.19e-31 and e = 1.602176634e-19 in (4. *. Float.pi *. e_0 *. h_ *. h_) /. (m_e *. e *. e)

(*c*)
let th x = let e_2x = exp (2. *. x) in (e_2x -. 1.) /. (e_2x +. 1.)
let argth x = (log ((1. +. x) /. (1. -. x))) /. 2.

(*Exercice 1.2*)

(*a*) 
(*"ahah" n'est pas la meme structure qu'un autre "ahah" meme si ils ont la meme valeur, de même "ah" est donc diférent de "ah"*)

(*b*)
(*true grace a l'evaluation paresseuse qui evite l'erreur*)

(*c*) 