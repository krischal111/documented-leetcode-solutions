use std::collections::HashSet;
use std::iter::FromIterator;
struct BusRoutes {
    bus_routes : Vec<HashSet<i32>>,
    no_of_bus : usize,
    bus_adjacent_list: Vec<Vec<usize>>,
}

impl BusRoutes {
    fn new(routes: Vec<Vec<i32>>) -> Self {
        let bus_routes : Vec<HashSet<i32>> = routes
            .iter()
            .map(|route| 
                HashSet::from_iter(route
                    .iter().cloned()
            )).collect();
        let no_of_bus = routes.len();
        let mut bus_adjacent_list:Vec<Vec<usize>> = (0..no_of_bus).map(|_| vec![]).collect();
        for i in 0 .. no_of_bus {
            for j in i+1 .. no_of_bus {
                if bus_routes[i].intersection(&bus_routes[j]).next().is_some() {
                    bus_adjacent_list[i].push(j);
                    bus_adjacent_list[j].push(i);
                }
            }
        }
        Self {
            bus_routes,
            no_of_bus,
            bus_adjacent_list,
        }
    }

    fn shortest_path(&self, source:i32, target:i32) -> i32 {
        if source == target {
            return 0
        }
        let mut visited_buses : HashSet<usize> = HashSet::new();
        let bus_of_node = |node| {
            let mut bus_of_node = Vec::new();
            for i in 0 .. self.no_of_bus {
                if self.bus_routes[i].contains(node) {
                    bus_of_node.push(i);
                }
            }
            bus_of_node
        };

        let mut queue = bus_of_node(&source);
        let target_buses : HashSet<usize> = HashSet::from_iter(bus_of_node(&target).iter().cloned());

        let mut count = 0;
        while  !!!queue.is_empty() {
            let mut next_queue = vec![];
            count += 1;

            for bus in queue.iter() {
                if visited_buses.contains(bus) {
                    continue;
                }
                if target_buses.contains(bus) {
                    return count;
                }
                for next_bus in self.bus_adjacent_list[*bus].iter() {
                    if visited_buses.contains(next_bus) {
                        continue;
                    }
                    next_queue.push(*next_bus);
                }
            }
            queue = next_queue;
        }
        return -1
    }
}

impl Solution {
    pub fn num_buses_to_destination(routes: Vec<Vec<i32>>, source: i32, target: i32) -> i32 {
        let bus_routes = BusRoutes::new(routes);
        return bus_routes.shortest_path(source, target);
    }
}


fn main() {
    let routes :Vec<Vec<i32>> = [[1,2,7],[3,6,7]].iter()
        .map(|v| 
            v
            .iter()
            .cloned()
            .collect())
        .collect();
    dbg!(Solution::num_buses_to_destination(routes, 1, 6));
}
struct Solution;