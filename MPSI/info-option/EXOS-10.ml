let deplace a b = Printf.printf " %d , %d  \n" a b

let rec hanoi n a b = match n with
  | 1 -> deplace a b
  | _ -> hanoi (pred n) a (3 - a - b) ; deplace a b ; hanoi (pred n) (3 - a - b) b 

let test = hanoi 4 0 2

let () = print_newline ()

let hanoii n a b = 
  let p = Stack.create () in
  Stack.push (n, a, b) p;
  while not (Stack.is_empty p) do
    match Stack.pop p with
      | 1 , x , y -> deplace x y
      | -1 , x , y -> deplace x y
      | m, x, y -> Stack.push (pred m , 3 - x -y , y) p ;Stack.push (-1 , x, y) p;  Stack.push (pred m , x , 3 - x -y) p
  done

let test = hanoii 4 0 
  

