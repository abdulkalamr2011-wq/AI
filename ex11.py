class MapColoringCSP:
    def __init__(self, regions, neighbors, colors):
        self.regions = regions          # List of variables (regions)
        self.neighbors = neighbors      # Dictionary mapping region to adjacent regions
        self.colors = colors            # Available colors domain
        self.assignment = {}            # Current color assignments

    def is_valid(self, region, color):
        """Check if assigning a color to a region violates any constraints."""
        for neighbor in self.neighbors.get(region, []):
            if neighbor in self.assignment and self.assignment[neighbor] == color:
                return False
        return True

    def backtrack(self):
        """Backtracking search to solve the CSP."""
        # If all regions are assigned, return the solution
        if len(self.assignment) == len(self.regions):
            return self.assignment

        # Select an unassigned region
        unassigned = [r for r in self.regions if r not in self.assignment]
        current_region = unassigned[0]

        # Try assigning each color from the domain
        for color in self.colors:
            if self.is_valid(current_region, color):
                self.assignment[current_region] = color
                
                # Recursively call backtrack
                result = self.backtrack()
                if result is not None:
                    return result
                
                # Undo assignment (backtrack)
                del self.assignment[current_region]

        return None

    def solve(self):
        return self.backtrack()

# Example Usage (Classic Australia Map Coloring Problem):
if __name__ == '__main__':
    regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    
    colors = ['Red', 'Green', 'Blue']
    
    # Adjacency constraints
    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    csp = MapColoringCSP(regions, neighbors, colors)
    solution = csp.solve()
    
    print("Map Coloring Solution:")
    for region, color in solution.items():
        print(f"{region} -> {color}")
