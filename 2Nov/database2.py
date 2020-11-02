from database import DB


def main():
    with DB('chinook.db') as connection:
        sql_str = """SELECT ar.Name, al.Title, t.Name, t.Milliseconds/1000 FROM artists ar
            JOIN albums al on ar.ArtistId = al.ArtistId
            JOIN tracks t on al.AlbumId = t.AlbumId
            WHERE t.Milliseconds/1000 < 1000
            ORDER BY al.Title
        """
        cursor = connection.cursor()
        cursor.execute(sql_str)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

if __name__ == '__main__':
    main()
