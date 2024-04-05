(*Exercice 9.1*)
(*a*)
let rot stack = 
  let r = Stack.create () in 
  Stack.push (Stack.pop stack) r ; 
  let rec store s = match Stack.is_empty s with
    |false -> Stack.pop s :: store s
    |true -> []
  in
  let rec pushs = function
    |h::t -> Stack.push h r ; pushs t
    |_ -> failwith "vide"
  in
  let () = pushs (store stack) in r 

  let teststack = Stack.create ()
  let () = for i = 0 to 9 do Stack.push i teststack done

  let () = Stack.iter print_int (rot teststack)

  (*push pop create is_empty*)