SEARCH = """
query ($search: String, $type: MediaType) {
  Media(search: $search, type: $type) {
        id
        type
        format
        title {
            native
            english
        }
        synonyms
        status
        description
        startDate {
            year
            month
            day
        }
        endDate {
            year
            month
            day
        }
        episodes
        chapters
        volumes
        coverImage {
            large
        }
        genres
        averageScore
        siteUrl
  }
}
"""

BY_ID = """
query ($id: Int, $type: MediaType) {
    Media(id: $id, type: $type) {
        id
        type
        format
        title {
            native
            english
        }
        synonyms
        status
        description
        startDate {
            year
            month
            day
        }
        endDate {
            year
            month
            day
        }
        episodes
        chapters
        coverImage {
            large
        }
        genres
        averageScore
  }
}
"""
