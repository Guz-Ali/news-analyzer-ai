package com.curatedNews.curatedNews.repositories;

import com.curatedNews.curatedNews.auth.model.AuthEntry;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AuthRepository extends JpaRepository<AuthEntry, String> {

}
