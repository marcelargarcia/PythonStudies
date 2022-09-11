from Tree.TreeNode import *

def build_product_tree():
    nilupul = TreeNode("Nilupul (CEO)")
    chinmay = TreeNode("Chinmay (CTO)")
    vishwa = TreeNode("Vishwa (Infrasctructure Head)")

    nilupul.add_child(chinmay)
    chinmay.add_child(vishwa)

    vishwa.add_child(TreeNode("Dhaval (Cloud Manager)"))
    vishwa.add_child(TreeNode("Abhijit (App Manager)"))

    chinmay.add_child(TreeNode("Aamir (Application Head)"))

    gels = TreeNode("Gels (HR Head)")
    gels.add_child(TreeNode("Peter (Recruitment Manager)"))
    gels.add_child(TreeNode("Waqas (Policy Manager)"))

    nilupul.add_child(gels)

    return nilupul

root = build_product_tree()
root.print_tree("name") # prints only name hierarchy
root.print_tree("designation") # prints only designation hierarchy
root.print_tree("both") # prints both (name and designation)
