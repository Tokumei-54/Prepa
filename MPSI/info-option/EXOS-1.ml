(*Exercice 1.1*)

(*a*) 
let x = 2.
let y = 
  let x_2 = x *. x in 
  let x_4 = x_2 *. x_2 in 
  x_4 *. x_4

(*b*)
let a_0 = 
  let e_0 = 8.85418782e-12 and
      h_ = 1.054571818e-34 and 
      m_e = 9.19e-31 and 
      e = 1.602176634e-19 
  in 
  4. *. Float.pi *. e_0 *. h_ *. h_ /. (m_e *. e *. e)

(*c*)
let th x = 
  let e_2x = exp (2. *. x) in
  (e_2x -. 1.) /. (e_2x +. 1.)

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
let volume n h b d = 
  if d > 2. *. h then
    failwith "Diametre trop grand volume null "
  else (
    let ha = (b /. 2.) /. tan (Float.pi /. n) in 
    let st = 0.5 *. b *. ha in 
    let sp = n *. st in 
    let sb = sp -. Float.pi *. (0.5 *. d ) ** 2. in 
    sb *. h
  )

let volume8 = volume 8.

let () = Printf.printf "l'anneau à un volume de %f m^3 \n" (volume8 54. 54. 54.)

(*Exercice 1.5*)

(*a*) 
let rec fact x = match x with  (*fonctione seulement jusqu'a 20! après la taille exède 2^62 et passe dans les negatifs*)
  | 0 -> 1
  | _ -> x * fact (pred x)

let tPasc l  =  
  for n  = 0  to l do
    for k = 0 to n do
      Printf.printf "%5d"  (fact n / (fact k * fact ( n - k )))
    done ;
    print_newline ()
  done

let tPasc2 l = 
  let p = Array.make ((l * (l+1))/2) 1 in
  print_endline ("1");
  print_endline ("1 1");
  for n  = 1  to (l-1) do
    print_string "1 ";
    for k = 1 to  n do
      p.((n * (n + 1)) / 2 + k) <- p.(((n - 1) * n) / 2 + k) + p.(((n-1) * (n))/2 + k -1);
      print_string (string_of_int p.((n * (n + 1)) / 2 + k)  ^ " ")
    done ;
    print_endline ("1")
  done

let () = print_string "nombre de lignes : " ; tPasc (read_int ())

(*Exercice 1.6*)
(*a*) (*&&*)
(*b*) (*5*)
(*c*) (*erreur and est silmultané donc x n'est pas definis*)
(*d*) (*erreur*)
(*e*) (* la fonction qui a x ,y associe y * (2 * x**2) *)
(*f*) (*1*)
(*g*) (*erreur*)
(*h*) (*erreur la fonction n'a pas eté initialisé comme réccursive *)
(*i*) (*3*)