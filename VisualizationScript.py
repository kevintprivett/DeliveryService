import csv
import datetime

import Package
import PackageHashTable
import Truck
import TourImageService


def main():
    # initialize a package hash table
    package_hash_table = PackageHashTable.PackageHashTable()

    # load data from packages.csv to package_hash_table
    load_package_data(package_hash_table)

    # initialize distance lookup table
    distances = {}

    # load data from distances.csv to distances dictionary
    load_distance_data(distances)

    # start clock on random day at 8 am, start of day
    current_time = datetime.datetime(2025, 1, 1, hour=8)

    # initialize trucks
    truck_1 = Truck.Truck("1", current_time, distances)

    # truck_1.load_package(package_hash_table.get(13))
    # truck_1.load_package(package_hash_table.get(14))
    # truck_1.load_package(package_hash_table.get(15))
    # truck_1.load_package(package_hash_table.get(16))
    # truck_1.load_package(package_hash_table.get(19))
    # truck_1.load_package(package_hash_table.get(20))
    # truck_1.load_package(package_hash_table.get(21))
    # truck_1.load_package(package_hash_table.get(34))
    # truck_1.load_package(package_hash_table.get(39))
    # truck_1.load_package(package_hash_table.get(1))
    # truck_1.load_package(package_hash_table.get(24))
    # truck_1.load_package(package_hash_table.get(27))
    # truck_1.load_package(package_hash_table.get(35))
    # truck_1.load_package(package_hash_table.get(12))

    for i in range(1, 41):
        truck_1.load_package(package_hash_table.get(i))

    # generate tour for truck_1
    # generate_tour modified to draw the tour for each optimization step

    # min_distance = 1000
    # min_seed = -1
    # for i in range (1000):
    #     truck_1.generate_tour(seed=i)
    #     this_distance = truck_1.calculate_total_distance(truck_1.tour)
    #     if this_distance < min_distance:
    #         min_distance = this_distance
    #         min_seed = i
    #     # print("total distance: ", this_distance)
    #     # TourImageService.TourImageService.draw_tour(truck_1.tour)
    #     truck_1.tour = []
    # print("min distance:", min_distance, ",min seed:", min_seed)

    truck_1.generate_tour(seed=10)


def load_package_data(package_hash_table):
    # load packages.csv

    with open('packages.csv', 'r', encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # create a package object using each line as input
            package = Package.Package(int(row[0]), row[1], row[2],
                                      row[3], row[4], row[5],
                                      row[6], row[7])

            # put package object in package_hash_table using id as key
            package_hash_table.put(package.id, package)


def load_distance_data(distances):
    # load distances.csv
    with open('distances.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            key = row[""]
            distances[key] = {k: float(v) for k, v in row.items() if k != ""}


if __name__ == "__main__":
    main()
