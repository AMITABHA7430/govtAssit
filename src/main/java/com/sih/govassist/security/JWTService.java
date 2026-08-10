package com.sih.govassist.security;

import com.sih.govassist.entity.User;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
import org.springframework.stereotype.Service;

import java.security.Key;
import java.util.Date;

@Service
public class JWTService {

    private final Key key = Keys.secretKeyFor(SignatureAlgorithm.HS256);

    public String generateToken(User user) {

        long expirationTime = 1000 * 60 * 60; // 1 hour

        return Jwts.builder()

                .claim("userId", user.getId())
                .claim("username", user.getName())

                .issuedAt(new Date())
                .expiration(
                        new Date(System.currentTimeMillis() + expirationTime)
                )
                .signWith(key)
                .compact();
    }
}