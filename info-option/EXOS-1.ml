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
(*b <> c*)

(*Exercice 1.3*)

(*a*) 
(*bool -> bool -> bool -> bool*)

(*b*)
let f a b c = (a || not b) && c

(*d*) 
(*a && b*)

(*Exercice 1.4*)

(*a*) 
let volume n h b d = let ha = (b /. 2.) /. tan (Float.pi /. n) in let st = 0.5 *. b *. ha in let sp = n *. st in let sb = sp -. Float.pi *. (0.5 *. d ) ** 2. in sb *. h
(*ffffffffffffffffffffiiiiiiiiiiiiiiiiiiiiiiiiiiinnnnnnnnnnnnnnnnnnniiiiiiiiiiiiiiiiiiiiiiirrrrrrrrrrrrrrrrrr*)
(*b*)
let volume8 h b d = volume 8. h b d

(*Exercice 1.5*)

(*a*) 
let rec fact x = match x with 
  | 0 -> 1
  | _ -> x * fact (pred x)

let tPasc l  = 
    for n  = 0  to l do
        for k = 0 to n do
          print_string (string_of_int (fact n / (fact k * fact ( n - k ))) ^ " ")
        done ;
        print_newline ()
    done

let () = print_string "nombre de lignes : " ; tPasc (read_int ())

(*Exercice 1.6*)
(*a*) (*erreur virgule*)
(*b*) (*5*)
(*c*) (*erreur and est silmultané donc x n'est pas definis*)
(*d*) (*erreur*)
(*e*) (* la fonction qui a x ,y associe y * (2 * x**2) *)
(*f*) (*1*)
(*g*) (*erreur*)
(*h*) (*erreur la fonction n'a pas eté initialisé comme réccursive *)
(*i*) (*3*)