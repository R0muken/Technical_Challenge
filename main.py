import argparse
from api_wrapper import BoredApiWrapper
from activity_dao import ActivityDatabase


def main():
    parser = argparse.ArgumentParser(description="Get an activity and save it in db")
    parser.add_argument("--type", help="Filter activities by type")
    parser.add_argument("--participants", type=int, help="Filter activities by the number of participants")
    parser.add_argument("--price", type=float, help="Filter activities by price")
    parser.add_argument("--accessibility", type=float, help="Filter activities by accessibility")
    parser.add_argument("--database-url", default='sqlite:///activity_db.sqlite', help="Database URL")
    parser.add_argument("command", choices=["list"],
                        help="Specify 'list' to get the last saved activities")
    args = parser.parse_args()

    api = BoredApiWrapper()
    db = ActivityDatabase(args.database_url)

    if args.command == "list":
        last_activities = db.get_latest_activities()
        print("Last Saved Activities:")
        for activity in last_activities:
            print(activity)
        return

    random_activity = api.random_activity(
        type=args.type,
        participants=args.participants,
        price=args.price,
        accessibility=args.accessibility
    )

    db.save_activity(
        activity_name=random_activity["activity"],
        type=random_activity["type"],
        participants=random_activity["participants"],
        price=random_activity["price"],
        link=random_activity["link"],
        key=random_activity["key"],
        accessibility=random_activity["accessibility"]
    )

    print("Random Activity:")
    print(random_activity)


if __name__ == "__main__":
    main()
