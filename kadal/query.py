MEDIA_SEARCH = """
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

MEDIA_BY_ID = """
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

MEDIA_PAGED = """
query ($id: Int, $page: Int, $perPage: Int, $search: String, $type: MediaType) {
  Page(page: $page, perPage: $perPage) {
    media(id: $id, search: $search, type: $type) {
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
      popularity
    }
  }
}
"""

USER_SEARCH = """
query ($search: String) {
  User(search: $search) {
    id
    name
    html_about: about(asHtml: true)
    about
    avatar {
      large
    }
    bannerImage
    siteUrl
    stats {
      watchedTime
      chaptersRead
    }
  }
}
"""

USER_BY_ID = """
query ($id: Int) {
  User(id: $id) {
    id
    name
    html_about: about(asHtml: true)
    about
    avatar {
      large
    }
    bannerImage
    siteUrl
    stats {
      watchedTime
      chaptersRead
    }
  }
}
"""
