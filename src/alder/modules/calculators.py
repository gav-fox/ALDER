def trees_per_cow(cow, tree, browse_percent):
    daily_dm = (cow.species_data["mature_liveweight_females"].value) * (cow.species_data["dry_matter_intake_dry_cows"].value / 100)
    annual_dm = (daily_dm * 365)
    tree_fodder_needed = (annual_dm)*(browse_percent/100)
    trees_needed = (tree_fodder_needed) / (tree.species_data["edible_yield"].value)
    return  trees_needed 





