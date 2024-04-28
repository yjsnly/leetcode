use std::rc::Rc;
use std::cell::RefCell;

#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}

struct Solution;

impl Solution {
    pub fn inorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut ans: Vec<i32> = vec![];
        let mut stack: Vec<Option<Rc<RefCell<TreeNode>>>> = vec![];
        if root.is_none() {
          return ans;
        }
        let mut p: Option<Rc<RefCell<TreeNode>>> = root.clone();
        while p.is_some() || !stack.is_empty() {
            while p.is_some() {
              stack.push(p.clone());
              p = p.clone().as_ref().unwrap().as_ref().borrow().left.clone();
            }
            p = stack.pop().unwrap();
            ans.push(p.clone().as_ref().unwrap().as_ref().borrow().val);
            p = p.clone().as_ref().unwrap().as_ref().borrow().right.clone();
        }
        return ans;
    }
}

fn main() {

}
