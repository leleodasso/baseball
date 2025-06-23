from database.DB_connect import DBConnect
from model.team import Team


class DAO():

    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select distinct year as anno
                    from teams t
                    where year >= 1980 """

        cursor.execute(query, ())

        for row in cursor:
            result.append(row["anno"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSquadreAnno(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *
                    from teams t
                    where year = %s """

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Team(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSalarioSquadre(u: Team, v: Team, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select sum(salary) as peso
                    from salaries s 
                    where year = %s
                    and (teamCode = %s or teamCode = %s)  """

        cursor.execute(query, (anno, u.teamCode, v.teamCode))

        for row in cursor:
            result.append(row["peso"])
        cursor.close()
        conn.close()
        return result