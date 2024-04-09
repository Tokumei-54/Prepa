let print_stack s = Stack.iter print_int s ; print_newline ()

let teststack = Stack.create ()
let () = for i = 0 to 9 do Stack.push i teststack done
let () = print_stack teststack


(*Exercice 9.1*)

(*a*)
let rot s = 
  let f = Stack.pop s in 
  let rec lister p = match Stack.is_empty p with
    |false -> let u = Stack.pop p in  u:: lister p
    |true -> []
  in
  let rec empiler = function 
    |h::t -> empiler t; Stack.push h s 
    |_ -> ()
  in
  let l = lister s in
  Stack.push f s ; empiler l; ()


let teststack = Stack.create ()
let () = for i = 0 to 9 do Stack.push i teststack done
let () = rot teststack 
let () = print_stack teststack

(*b*)
let rec rotk n s = match n with
  | 0 -> ()
  | _ -> rot s ; rotk (pred n) s

let teststack = Stack.create ()
let () = for i = 0 to 9 do Stack.push i teststack done
let () = rotk 3 teststack 
let () = print_stack teststack

(*c*)
let swap s = let e1 = Stack.pop s in let e2 = Stack.pop s in Stack.push e1 s; Stack.push e2 s  

let teststack = Stack.create ()
let () = for i = 0 to 9 do Stack.push i teststack done
let () = swap teststack
let () = print_stack teststack

(*d*)
let swapk n s = 