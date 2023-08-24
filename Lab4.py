class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def search_by_team(self, team_name):
        return [match for match in self.matches if team_name in [match.team1, match.team2]]

    def search_by_location(self, location):
        return [match for match in self.matches if match.location == location]

    def search_by_timing(self, timing):
        return [match for match in self.matches if match.timing == timing]

def main():
    table = FlightTable()

    table.add_match(Match("Mumbai", "India", "Sri Lanka", "DAY"))
    table.add_match(Match("Delhi", "England", "Australia", "DAY-NIGHT"))
    table.add_match(Match("Chennai", "India", "South Africa", "DAY"))
    table.add_match(Match("Indore", "England", "Sri Lanka", "DAY-NIGHT"))
    table.add_match(Match("Mohali", "Australia", "South Africa", "DAY-NIGHT"))
    table.add_match(Match("Delhi", "India", "Australia", "DAY"))

    while True:
        print("Choose search parameter:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            team_name = input("Enter the team name: ")
            team_matches = table.search_by_team(team_name)
            print(f"Matches for team {team_name}:")
            if team_matches:
                for match in team_matches:
                    print(f"{match.team1} vs {match.team2} at {match.location}, {match.timing}")
            else:
                print("No matches found for the given team.")
        
        elif choice == 2:
            location = input("Enter the location: ")
            location_matches = table.search_by_location(location)
            print(f"Matches at location {location}:")
            if location_matches:
                for match in location_matches:
                    print(f"{match.team1} vs {match.team2} at {match.location}, {match.timing}")
            else:
                print("No matches found for the given location.")

        elif choice == 3:
            timing = input("Enter the timing: ")
            timing_matches = table.search_by_timing(timing)
            print(f"Matches at timing {timing}:")
            if timing_matches:
                for match in timing_matches:
                    print(f"{match.team1} vs {match.team2} at {match.location}, {match.timing}")
            else:
                print("No matches found for the given timing.")
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
        
        cont = input("Do you want to search again? (yes/no): ")
        if cont.lower() != "yes":
            break

if __name__ == "__main__":
    main()
