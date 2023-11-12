struct Graph {
    adj_list : Vec<Vec<(i32, i32)>>,
}
/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Graph {
    fn new(n: i32, edges: Vec<Vec<i32>>) -> Self {
        let mut adj_list = vec![vec![];n as usize];
        for edge in edges {
            let (node1, node2, cost) = (edge[0], edge[1], edge[2]);
            adj_list[node1 as usize].push((node2, cost));
        }
        return Self {
            adj_list,
        };
    }

    #[inline]
    fn add_edge(&mut self, edge: Vec<i32>) {
        let (node1, node2, cost) = (edge[0], edge[1], edge[2]);
        self.adj_list[node1 as usize].push((node2, cost));
    }
    
    fn shortest_path(&self, node1: i32, node2: i32) -> i32 {
        use std::collections::HashSet;
        struct Queue {
            distance : i32,
            node : i32,
        }
        use std::cmp::Ordering;
        impl Ord for Queue {
            fn cmp(&self, other: &Self) -> Ordering {
                other.distance.cmp(&self.distance)
            }
        }
        impl PartialOrd for Queue {
            fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
                other.distance.partial_cmp(&self.distance)
            }
        }
        impl PartialEq for Queue {
            fn eq(&self, other: &Self) -> bool {
                other.distance == self.distance
            }
        }
        impl Eq for Queue {}

        let mut queue = std::collections::BinaryHeap::new();
        queue.push(Queue {distance: 0, node: node1});
        let mut visited = HashSet::new();
        while !queue.is_empty() {
            let Queue {distance, node} = queue.pop().unwrap();

            if node == node2 {
                return distance;
            }

            visited.insert(node);
            for (children_node, weight) in self.adj_list[node as usize].iter() {
                if visited.contains(children_node) {
                    continue;
                }
                let distance = weight + distance;
                queue.push(Queue {distance, node: *children_node});
            }
        }

        return -1;
        
    }
}

// /**
//  * Your Graph object will be instantiated and called as such:
//  * let obj = Graph::new(n, edges);
//  * obj.add_edge(edge);
//  * let ret_2: i32 = obj.shortest_path(node1, node2);
//  */
// struct Solution;
// fn main() {
//     let mut g = Graph::new(6, vec!)
//     testcase = [[6,[[3,5,990551],[1,3,495721],[0,1,985797],[4,5,422863],[4,1,505663]]],[0,1],[3,5],[4,4],[0,3],[[5,0,250117]],[4,5],[[3,1,142005]],[2,2],[4,0],[[2,0,124744]],[[5,1,74396]],[3,3],[[3,2,571238]],[[1,4,3408]],[[0,4,832]],[[5,2,417]],[2,2],[2,4],[[2,3,80]],[[5,4,6]],[3,4],[[4,3,837171]],[[1,2,162278]],[[3,4,1]],[2,0],[[0,3,1]],[0,4],[3,5],[1,1],[3,4],[[4,2,1]],[[2,1,1]]];
// }